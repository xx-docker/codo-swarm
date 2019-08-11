#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : shenshuo
date   : 2017-10-11
role   : Application
"""

from websdk.application import Application as myApplication
from biz.handlers.asset_server_handler import asset_server_urls
from biz.handlers.asset_db_handler import asset_db_urls
from biz.handlers.admin_user_handler import admin_user_urls
from biz.handlers.asset_tag_handler import tag_urls
from biz.handlers.system_user_handler import system_user_urls
from biz.handlers.asset_configs_handler import asset_configs_urls
from biz.handlers.hand_update_asset_handler import asset_hand_server_urls

class Application(myApplication):
    def __init__(self, **settings):
        urls = []
        urls.extend(asset_server_urls)
        urls.extend(asset_db_urls)
        urls.extend(admin_user_urls)
        urls.extend(tag_urls)
        urls.extend(system_user_urls)
        urls.extend(asset_configs_urls)
        urls.extend(asset_hand_server_urls)
        super(Application, self).__init__(urls, **settings)


if __name__ == '__main__':
    pass
