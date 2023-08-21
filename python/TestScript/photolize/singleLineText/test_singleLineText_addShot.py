# 単一行テキストの配置確認（配置設定を変えた時に実行すべきファイル）
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


class TestSingleLineText_addShot():
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
    # photolizeにログインする
    self.driver.get("https://saruya:saruya@staging-user.photolize.jp/login/basic_auth")
    self.driver.get("https://staging-user.photolize.jp/login")
    self.driver.set_window_size(1463, 1032)
    self.driver.find_element(By.ID, "input-7").click()
    self.driver.find_element(By.ID, "input-7").send_keys("company_code26")
    self.driver.find_element(By.CSS_SELECTOR, ".v-btn__content").click()
    self.driver.find_element(By.ID, "input-11").send_keys("aridome")
    self.driver.find_element(By.ID, "input-14").send_keys("aridome")
    self.driver.find_element(By.CSS_SELECTOR, ".btn > .v-btn__content").click()
    # 有留アプリテストを選択
    self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/main/div/div[2]/div[2]/div/div[13]/a/div/div/div[2]/div").click()
    # 新規レコードを選択
    self.driver.find_element(By.CSS_SELECTOR, ".v-btn__content > span").click()
    time.sleep(5)
    # 新規レコードを保存
    self.driver.find_element(By.CSS_SELECTOR, ".fa-floppy-disk > path").click()
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".theme--light:nth-child(2) > .v-btn__content"))).click()
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".v-card__actions:nth-child(2) .v-btn__content"))).click()
    # 最新のビューを選択
    self.driver.find_element(By.CSS_SELECTOR, ".ag-row-even:nth-child(1) .mr-1:nth-child(2) .v-icon").click()
    # スクリーンショットをとる
    save_screenShot(self)
    time.sleep(3) # 目視確認
    # ログアウトする
    self.driver.find_element(By.CSS_SELECTOR, ".v-avatar > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".v-btn--text > .v-btn__content").click()
    # 画面を閉じる
    self.driver.close()

def save_screenShot(self):
  # 保存先ディレクトリを指定
  output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img/")
  # フォルダが存在しない場合は作成
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)
  # 現在の日付を取得してフォーマット
  current_date = datetime.now().strftime("%m-%d_%H-%M-%S")
  # ファイル名を生成
  output_file_name = f"SLT_view_af_{current_date}.png"

  # ファイルパスを作成
  output_file_path = os.path.join(output_dir, output_file_name)
  
  # # get width and height of the page
  # w = self.driver.execute_script("return document.body.scrollWidth;")
  # h = self.driver.execute_script("return document.body.scrollHeight;")

  # # set window size
  # self.driver.set_window_size(w,h)

  # 追加: ここでフルページのスクリーンショットを取る
  self.driver.save_screenshot(output_file_path)

  print("")
  print(f"単一行テキストの配置画像を{output_file_path}に保存しました")
