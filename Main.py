# -*- coding: utf-8 -*-

from CPublishmanager import CPublish_manager_byr
from CPublishmanager import CPublish_manager_newsmth
from CPublishmanager import CPublish_manager_buaaer
from CPublishmanager import CPublish_manager_bjtu

if __name__ == "__main__":
    manager_byr = CPublish_manager_byr("byr")
    manager_byr.do_publish()

    manager_newsmth = CPublish_manager_newsmth("newsmth")
    manager_newsmth.do_reply()

    manager_buaaer = CPublish_manager_buaaer("buaaer")
    manager_buaaer.do_publish()

    manager_buaaer = CPublish_manager_bjtu("bjtu")
    manager_buaaer.do_publish()