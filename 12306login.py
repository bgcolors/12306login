from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://kyfw.12306.cn/otn/login/init')
username = browser.find_element(by=By.ID, value="username")
username.send_keys('bogevv')
password = browser.find_element(by=By.ID, value="password")
password.send_keys('123talentisme06')
i = raw_input()
if i == '':
    browser.find_element(by=By.ID, value="loginSub").click()