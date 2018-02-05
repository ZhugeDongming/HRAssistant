__author__ = 'Dongming'
# encoding: utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import ConfigParser

class CPublisher:
    def __init__(self):
        self.chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        self.browser = webdriver.Chrome(executable_path=self.chrome_driver)
        self.login_stat = False

    def login(self , url , name , passwd , login_element ):
        self.browser.get( url )

        locator = (By.ID, login_element.get('ID_login_id') )
        if( self.wait_for_load( locator ) == True):
            #u_login_id
            self.browser.find_element_by_id(login_element.get('ID_login_id')).send_keys( name )
            #u_login_passwd
            self.browser.find_element_by_id(login_element.get('ID_login_passwd')).send_keys( passwd )
            #u_login_submit
            self.browser.find_element_by_id(login_element.get('ID_login_button')).click()
        else:
            print "[Error]Wait for Login page Failed!"

        locator = (By.XPATH,login_element.get('XPATH_login_state') )
        if(self.wait_for_load(locator) == True):
            self.login_stat = True
        else:
            print "[Error]Wait for Logined page Failed!"


    def publish_artical(self , url , subject ,content , post_element):
        print("[Debug]navigate begin:" + url)
        self.browser.set_page_load_timeout(3)
        try:
            self.browser.get( url )
        except:
            self.browser.execute_script('window.stop()')
        print("[Debug]navigate end:" + url)

        # 新主题
        link = post_element.get('XPATH_new_article_button')
        locator = (By.XPATH , link )
        if(self.wait_for_load(locator) == True):
            self.browser.find_element_by_xpath( link ).click()

        # 找到编辑框
        locator = (By.ID,post_element.get('ID_post_subject'))
        if(self.wait_for_load(locator) == True):
            print("[Debug]Page Load success!")
            self.browser.find_element_by_id(post_element.get('ID_post_subject')).send_keys( subject)

            self.browser.find_element_by_id(post_element.get('ID_post_content')).send_keys( content)

            self.browser.find_element_by_css_selector(post_element.get('CSS_input_button')).click()
            time.sleep(5)


    def wait_for_load(self, locator ):
        try:
            WebDriverWait(self.browser, 10, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except NoSuchElementException:
            return False
        # finally:
        #     self.browser.close()

    def IsLogin(self):
        bret = self.browser.find_element_by_xpath("//*[@id='m_inbox']")


    def __del__(self):
        self.browser.quit()
        print "[Debug]finish"

