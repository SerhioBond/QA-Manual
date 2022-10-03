from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


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

elem = WebDriverWait(driver, 10).until(EC.title_contains("Hillel"))

if elem:
  print ("OK")
  not_found = True
else:
  print ("Element not found")
  not_found = False

assert not_found
driver.close()