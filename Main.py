# -*- coding: utf-8 -*-

from CPublishmanager import CPublish_manager_byr
from CPublishmanager import CPublish_manager_newsmth

if __name__ == "__main__":
    manager_byr = CPublish_manager_byr()
    manager_byr.do_publish()

    manager_newsmth = CPublish_manager_newsmth()
    #manager_newsmth.do_publish()
    manager_newsmth.do_reply()
