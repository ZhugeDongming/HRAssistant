__author__ = 'Dongming'
# encoding: utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
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

    def parese_element(self , element ):
        array = element.split(",")
        element_type = array[0].strip()
        value = array[1].strip()
        if( element_type == "ID"):
            return "ID" , value
        elif( element_type == "CSS" ):
            return "CSS" , value
        elif( element_type == "XPATH" ):
            return "XPATH" , value

    def set_locator(self , element):
        (k, v) = self.parese_element(element)
        if( k == "ID"):
            locator = (By.ID, v )
            return locator
        elif( k == "CSS" ):
            locator = (By.CSS_SELECTOR, v )
            return locator
        elif( k == "XPATH" ):
            locator = (By.XPATH,  v )
            return locator

    def get_element(self , element ):
        (k, v) = self.parese_element(element)
        if( k == "ID"):
            return  self.browser.find_element_by_id(v)
        elif( k == "CSS" ):
            return  self.browser.find_element_by_css_selector(v)
        elif( k == "XPATH" ):
            return  self.browser.find_element_by_xpath(v)



    def login(self , url , name , passwd , login_element ):
        self.browser.get( url )

        locator = self.set_locator( login_element.get('element_id'))

        if( self.wait_for_load( locator ) == True):
            ctrl = self.get_element(login_element.get('element_id'))
            ctrl.send_keys( name )

            ctrl = self.get_element(login_element.get('element_passwd'))
            ctrl.send_keys( passwd )

            ctrl = self.get_element(login_element.get('element_button'))
            ctrl.click()
        else:
            print "[Error]Wait for Login page Failed!"

        locator = self.set_locator( login_element.get('element_state'))
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
        locator = self.set_locator( post_element.get('element_new_article_button'))
        if(self.wait_for_load(locator) == True):
            ctrl = self.get_element(post_element.get('element_new_article_button'))
            ctrl.click()

        # 找到编辑框
        locator = self.set_locator( post_element.get('element_post_subject'))
        if(self.wait_for_load(locator) == True):
            print("[Debug]Page Load success!")
            ctrl = self.get_element(post_element.get('element_post_subject'))
            ctrl.send_keys( subject)

            ctrl = self.get_element(post_element.get('element_post_content'))
            ctrl.send_keys( content)

            ctrl = self.get_element(post_element.get('element_input_button'))
            ctrl.click()

            time.sleep(5)

    def reply_artical(self , url , content , post_element ):
        print("[Debug]navigate begin:" + url)
        self.browser.set_page_load_timeout(3)
        try:
            self.browser.get( url )
        except:
            self.browser.execute_script('window.stop()')
        print("[Debug]navigate end:" + url)

        # 回复
        locator = self.set_locator( post_element.get('element_reply_content'))
        #locator = (By.CSS_SELECTOR , "textarea[id='quick_text']" )
        if(self.wait_for_load(locator) == True):
            ctrl = self.get_element(post_element.get('element_reply_content'))
            ctrl.send_keys( content)

            ctrl = self.get_element(post_element.get('element_reply_submit'))
            ctrl.click()

            #self.browser.find_element_by_xpath( "textarea[id='quick_text']" ).send_keys(content)
            #self.browser.find_element_by_css_selector("td[id='quick_submit'] input").click()

            time.sleep(5)


    def wait_for_load(self, locator ):
        try:
            WebDriverWait(self.browser, 10, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        # finally:
        #     self.browser.close()

    def IsLogin(self):
        bret = self.browser.find_element_by_xpath("//*[@id='m_inbox']")


    def __del__(self):
        self.browser.quit()
        print "[Debug]finish"

