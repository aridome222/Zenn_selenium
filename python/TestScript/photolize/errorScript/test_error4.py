# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

class Testerror4():
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
  
  def test_addNewRecord(self):
    self.driver.get("https://saruya:saruya@staging-user.photolize.jp/login/basic_auth")
    self.driver.get("https://staging-user.photolize.jp/login")
    self.driver.set_window_size(1463, 1032)
    self.driver.find_element(By.ID, "input-7").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "input-7").send_keys("company_code26")
    self.driver.find_element(By.CSS_SELECTOR, ".v-btn__content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "input-11").send_keys("aridome")
    self.driver.find_element(By.ID, "input-14").send_keys("aridome")
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn > .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".btn > .v-btn__content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".py-0:nth-child(2) .relative")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.execute_script("window.scrollTo(0,317)")
    element = self.driver.find_element(By.CSS_SELECTOR, ".py-0:nth-child(12) .v-list-item__title")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".py-0:nth-child(12) .v-list-item__title").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "新規レコード追加").click()
    self.driver.find_element(By.CSS_SELECTOR, ".input").click()
    # 指定したIDの要素がクリック可能になるまで待機
    element = self.driver.find_element(By.ID, "input-221")
    self.driver.execute_script("arguments[0].click();", element)
    time.sleep(2)
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(6) .v-card__actions .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
    self.driver.find_element(By.ID, "input-221").send_keys("お寿司")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(6) .v-card__actions .v-btn__content").click()
    time.sleep(2)
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
    time.sleep(2)
    self.driver.execute_script("window.scrollTo(0,200)")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .cbbox").click()
    time.sleep(2)
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .cbbox")
    time.sleep(2)
    actions = ActionChains(self.driver)
    time.sleep(2)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .cbbox").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(16) .v-card__actions .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(16) .v-card__actions .v-btn__content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".radafdad").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".v-radio:nth-child(3) .v-input--selection-controls__ripple").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".v-dialog__content:nth-child(10) .v-card__actions .v-btn__content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-btn--is-elevated > .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".v-btn--is-elevated > .v-btn__content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".theme--light:nth-child(2) > .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".theme--light:nth-child(2) > .v-btn__content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-card__actions:nth-child(2) .v-btn__content")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".v-card__actions:nth-child(2) .v-btn__content").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-avatar > img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".v-avatar > img").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".v-btn--text")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".v-btn--text").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.close()
  
