from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver   
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

options=Options()
options.add_argument('start-maximized')
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get('https://www.youtube.com/watch?v=kHslscqoxvA')
time.sleep(2)
driver.find_element(by=By.XPATH,value="/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[27]/div[2]/div[1]/button").click()
time.sleep(200)