# 単一行テキストの「初期値／編集」の設定操作テスト
# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.keys import Keys
import json
import os
from datetime import datetime
import difflib


class Test_chg_setting_initValue():
  def setup_method(self, method):
    options = Options()
    # options.add_argument('--headless')  # ヘッドレスモードでブラウザを起動
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub', options=options)
    self.driver.implicitly_wait(10) # 10秒まで待機する
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_singlelinetext(self):    
    # photolize管理画面にログインする
    self.driver.get("https://saruya:saruya@staging-admin.photolize.jp/login")
    self.driver.set_window_size(1463, 1032)
    self.driver.find_element(By.ID, "admin_user_code").send_keys("admin_test")
    self.driver.find_element(By.ID, "password").send_keys("31g8ar7p")
    self.driver.find_element(By.CSS_SELECTOR, ".uk-button").click()
    # 有留テストアプリに移動する
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "アプリ一覧を見る")))
    self.driver.find_element(By.LINK_TEXT, "アプリ一覧を見る").click()
    self.driver.get("https://staging-admin.photolize.jp/admin/appli/edit_vue/151")
    # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "有留テストアプリ")))
    # element = self.driver.find_element(By.ID, "item_151")
    # link = element.find_element(By.LINK_TEXT, "有留テストアプリ")
    # self.driver.execute_script("arguments[0].click();", link)
    # 単一行テキスト1を選択
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[4]/div/div/div")))
    self.driver.find_element(By.XPATH, "//div[4]/div/div/div").click()

    time.sleep(2)
    ### 「初期値／編集」 ###
    # テキストボックス内の文字を消して新しく文字を入力
    element = self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > input")
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > input").send_keys("テスト１")
    time.sleep(3)

    # 保存する
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-btn:nth-child(9)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".mdi-content-save").click()
    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    assert self.driver.switch_to.alert.text == "保存しました"
    self.driver.switch_to.alert.accept()
    # アプリ一覧画面に戻る
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-list-item:nth-child(1) > .v-list-item__title")
    self.driver.execute_script("arguments[0].click();", element)
    WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    assert self.driver.switch_to.alert.text == "アプリ一覧にもどってもよろしいでしょうか？保存されていないデータは消失します。"
    self.driver.switch_to.alert.accept()
    # ログアウトして画面を閉じる
    self.driver.find_element(By.LINK_TEXT, "テストマニュアル管理者").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.close()
