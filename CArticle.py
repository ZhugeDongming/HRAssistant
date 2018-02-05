__author__ = 'Dongming'
# encoding: utf-8

import sys,os
import ConfigParser

class CArticle:
    def __init__(self , url , subject , content):
        self.pub_url = url
        self.subject = subject
        self.content = content

    def set_subject(self , subject ):
        self.subject = subject

    def set_content(self , content):
        self.content = content

    def set_url(self , url ):
        self.pub_url = url

class CArticleManager:
    def __init__(self):
        self.list_article = []
        self.count = 0

    def load_article_path(self , ini_file_path ):
        cf = ConfigParser.ConfigParser()
        cf.read(ini_file_path)

        dic = ini_file_path[:ini_file_path.rfind("/")]
        print dic

        s = cf.sections()
        print 'section:', s

        o = cf.options("summary")
        print 'options:', o

        v = cf.items("summary")
        print 'db:', v

        count = cf.getint("summary", "count")
        for i in range(1,count+1):
            #path =  + cf.get( str(i), "filepath")
            path = dic + "/" + cf.get( str(i), "filepath")
            self.load_article(path)


    def load_article(self , data_file_path ):
        content = ""
        f = open( data_file_path )
        url = f.readline().decode("utf-8")
        # 去掉\n，否则会导致输入的时候把\n当做回车输入
        subject = f.readline().decode("utf-8").replace("\n","")
         # 拼接content内容
        line = f.readline()
        while line:
            content = content + line
            line = f.readline()
        content = content.decode("utf-8").replace("\t", "    ")
        article = CArticle( url , subject , content )
        print( url , subject , content)
        self.list_article.append(article)
