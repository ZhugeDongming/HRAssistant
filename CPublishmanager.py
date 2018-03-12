__author__ = 'Dongming'
# encoding: utf-8

import ConfigParser
from CArticle import CArticleManager
from CPublisher import CPublisher

CONFIG_KEY = [ "login_url" ,
               "login_name",
               "login_password",
               "element_id",
               "element_passwd",
               "element_button",
               "element_state",
               "element_post_subject",
               "element_post_content",
               "element_input_button",
               "element_new_article_button",
               "element_reply_content",
               "element_reply_submit"
               ]

class CPublish_manager:
    def __init__(self , section_name ):
        self.login_url = ''
        self.login_name = ''
        self.login_password = ''
        self.section_name = section_name
        self.element = dict()
        self.article_manager = CArticleManager()
        self.load_config('./config/config.ini')


    def  load_config(self, config_file_path):
        section_name = self.section_name
        cf = ConfigParser.ConfigParser()
        cf.read(config_file_path)

        s = cf.sections()
        print 'section:', s

        o = cf.options(section_name)
        print 'options:', o

        v = cf.items(section_name)
        print 'db:', v


        self.login_url = cf.get(section_name, CONFIG_KEY[0])
        self.login_name = cf.get(section_name, CONFIG_KEY[1])
        self.login_password = cf.get(section_name, CONFIG_KEY[2])

        length = len(CONFIG_KEY)
        for i in range(3 , length) :
            try:
                self.element.setdefault(  CONFIG_KEY[i], cf.get(section_name, CONFIG_KEY[i]))
            except:
                continue


    def do_publish(self):
        for i in self.article_manager.list_article:
            publisher = CPublisher()
            publisher.login( self.login_url ,self.login_name , self.login_password , self.element)
            publisher.publish_artical( i.pub_url ,i.subject , i.content , self.element)
            del publisher



class CPublish_manager_byr(CPublish_manager):
    def __init__(self , setion_name):
        CPublish_manager.__init__(self , setion_name)
        self.article_manager.load_article_path("./config/byr.ini")

class CPublish_manager_newsmth(CPublish_manager):
    def __init__(self , setion_name):
        CPublish_manager.__init__(self , setion_name)
        self.article_manager.load_article_path("./config/newsmth.ini")

    def do_reply(self):
        for i in self.article_manager.list_article:
            publisher = CPublisher()
            publisher.login( self.login_url ,self.login_name , self.login_password , self.element)
            publisher.reply_artical( i.pub_url ,"up" )
            del publisher

class CPublish_manager_buaaer(CPublish_manager):
    def __init__(self , setion_name):
        CPublish_manager.__init__(self , setion_name)
        self.article_manager.load_article_path("./config/buaaer.ini")

class CPublish_manager_bjtu(CPublish_manager):
    def __init__(self , setion_name):
        CPublish_manager.__init__(self , setion_name)
        self.article_manager.load_article_path("./config/bjtu.ini")