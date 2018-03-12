# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

if __name__ == "__main__":
    # manager_byr = CPublish_manager_byr()
    # manager_byr.do_publish()

    manager_newsmth = CPublish_manager_newsmth()
    #manager_newsmth.do_publish()
    manager_newsmth.do_reply()
