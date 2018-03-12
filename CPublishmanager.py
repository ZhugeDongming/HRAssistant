__author__ = 'Dongming'
# encoding: utf-8

import ConfigParser
from CArticle import CArticleManager
from CPublisher import CPublisher

class CPublish_manager_byr:
    def __init__(self):
        self.login_url = ''
        self.login_name = ''
        self.login_password = ''

        self.login_element = dict()
        self.post_element = dict()
        self.article_manager = CArticleManager()
        self.article_manager.load_article_path("./config/byr.ini")
        self.load_config('./config/config.ini')

    def  load_config(self, config_file_path):
        section_name = "byr"
        cf = ConfigParser.ConfigParser()
        cf.read(config_file_path)

        s = cf.sections()
        print 'section:', s

        o = cf.options("byr")
        print 'options:', o

        v = cf.items("byr")
        print 'db:', v

        self.login_url = cf.get(section_name, "login_url")
        self.login_name = cf.get(section_name, "login_name")
        self.login_password = cf.get(section_name, "login_password")

        self.login_element.setdefault(  "ID_login_id", cf.get(section_name, "ID_login_id"))
        self.login_element.setdefault(  "ID_login_passwd", cf.get(section_name, "ID_login_passwd"))
        self.login_element.setdefault(  "ID_login_button", cf.get(section_name, "ID_login_button"))
        self.login_element.setdefault(  "XPATH_login_state", cf.get(section_name, "XPATH_login_state"))

        self.post_element.setdefault(  "ID_post_subject", cf.get(section_name, "ID_post_subject"))
        self.post_element.setdefault(  "ID_post_content", cf.get(section_name, "ID_post_content"))
        self.post_element.setdefault(  "CSS_input_button", cf.get(section_name, "CSS_input_button"))
        self.post_element.setdefault(  "XPATH_new_article_button", cf.get(section_name, "XPATH_new_article_button"))
        self.post_element.setdefault(  "XPATH_post_subject", cf.get(section_name, "XPATH_post_subject"))

    def do_publish(self):
        for i in self.article_manager.list_article:
            publisher = CPublisher()
            publisher.login( self.login_url ,self.login_name , self.login_password , self.login_element)
            publisher.publish_artical( i.pub_url ,i.subject , i.content , self.post_element)
            del publisher

class CPublish_manager_newsmth:
    def __init__(self):
        self.login_url = ''
        self.login_name = ''
        self.login_password = ''

        self.login_element = dict()
        self.post_element = dict()
        self.article_manager = CArticleManager()
        self.article_manager.load_article_path("./config/newsmth.ini")
        self.load_config('./config/config.ini')

    def  load_config(self, config_file_path):
        section_name = "newsmth"
        cf = ConfigParser.ConfigParser()
        cf.read(config_file_path)

        s = cf.sections()
        print 'section:', s

        o = cf.options(section_name)
        print 'options:', o

        v = cf.items(section_name)
        print 'db:', v

        self.login_url = cf.get(section_name, "login_url")
        self.login_name = cf.get(section_name, "login_name")
        self.login_password = cf.get(section_name, "login_password")

        self.login_element.setdefault(  "ID_login_id", cf.get(section_name, "ID_login_id"))
        self.login_element.setdefault(  "ID_login_passwd", cf.get(section_name, "ID_login_passwd"))
        self.login_element.setdefault(  "ID_login_button", cf.get(section_name, "ID_login_button"))
        self.login_element.setdefault(  "XPATH_login_state", cf.get(section_name, "XPATH_login_state"))

        self.post_element.setdefault(  "ID_post_subject", cf.get(section_name, "ID_post_subject"))
        self.post_element.setdefault(  "ID_post_content", cf.get(section_name, "ID_post_content"))
        self.post_element.setdefault(  "CSS_input_button", cf.get(section_name, "CSS_input_button"))
        self.post_element.setdefault(  "XPATH_new_article_button", cf.get(section_name, "XPATH_new_article_button"))
        self.post_element.setdefault(  "XPATH_post_subject", cf.get(section_name, "XPATH_post_subject"))

    def do_publish(self):
        for i in self.article_manager.list_article:
            publisher = CPublisher()
            publisher.login( self.login_url ,self.login_name , self.login_password , self.login_element)
            publisher.publish_artical( i.pub_url ,i.subject , i.content , self.post_element)
            del publisher

    def do_reply(self):
        for i in self.article_manager.list_article:
            publisher = CPublisher()
            publisher.login( self.login_url ,self.login_name , self.login_password , self.login_element)
            publisher.reply_artical( i.pub_url ,"up" )
            del publisher

