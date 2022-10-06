from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import re


options = Options()
# options.add_argument("start-maximized"); # open Browser in maximized mode
# options.add_argument("disable-infobars"); # disabling infobars
# options.add_argument("--disable-extensions"); # disabling extensions
# options.add_argument("--disable-gpu"); # applicable to windows os only
# options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service('D:\\QA\\ChromeDriver\\chromedriver.exe'), options=options)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[class*='sign']")))
if elem.is_displayed():
  elem.click()
else:
  print ("Element not found")

elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[id$='Email']")))
if elem.is_displayed():
  elem.send_keys("xebebe5732@zfobo.com")
else:
  print ("Element not found")

elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[id$='Password']")))
if elem.is_displayed():
  elem.send_keys("Parolqaauto")
else:
  print ("Element not found")

elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "*[class^='btn btn-primary']")))
if elem.is_displayed():
  elem.click()
else:
  print ("Element not found")

elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='h3 panel-empty_message']"))).get_attribute("innerHTML")
if elem:
  result = re.search(r'^You don’t', elem)
  assert result
else:
  print ("Element not found")

driver.close()