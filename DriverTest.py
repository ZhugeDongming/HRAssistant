# coding = utf-8

from time import sleep
from selenium import webdriver

chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver)
browser.implicitly_wait(26)
browser.get('https://bbs.byr.cn/')

sleep(5)
browser.quit()