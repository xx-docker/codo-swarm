#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
Author : shenshuo
Date   : 2017-10-11 12:58:26
Desc   : 配置文件
"""

import os
from websdk.consts import const

ROOT_DIR = os.path.dirname(__file__)
debug = True
xsrf_cookies = False
expire_seconds = 365 * 24 * 60 * 60
cookie_secret = '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2X6TP1o/Vo='

DEFAULT_DB_DBHOST = os.getenv('DEFAULT_DB_DBHOST', '172.16.0.223')
DEFAULT_DB_DBPORT = os.getenv('DEFAULT_DB_DBPORT', '3306')
DEFAULT_DB_DBUSER = os.getenv('DEFAULT_DB_DBUSER', 'root')
DEFAULT_DB_DBPWD = os.getenv('DEFAULT_DB_DBPWD', 'ljXrcyn7chaBU4F')
DEFAULT_DB_DBNAME = os.getenv('DEFAULT_DB_DBNAME', 'do_task')

READONLY_DB_DBHOST = os.getenv('READONLY_DB_DBHOST', '172.16.0.223')
READONLY_DB_DBPORT = os.getenv('READONLY_DB_DBPORT', '3306')
READONLY_DB_DBUSER = os.getenv('READONLY_DB_DBUSER', 'root')
READONLY_DB_DBPWD = os.getenv('READONLY_DB_DBPWD', 'ljXrcyn7chaBU4F')
READONLY_DB_DBNAME = os.getenv('READONLY_DB_DBNAME', 'do_task')

DEFAULT_REDIS_HOST = os.getenv('DEFAULT_REDIS_HOST', '172.16.0.223')
DEFAULT_REDIS_PORT = os.getenv('DEFAULT_REDIS_PORT', '6379')
DEFAULT_REDIS_DB = 8
DEFAULT_REDIS_AUTH = True
DEFAULT_REDIS_CHARSET = 'utf-8'
DEFAULT_REDIS_PASSWORD = os.getenv('DEFAULT_REDIS_PASSWORD', '123456')

DEFAULT_MQ_ADDR = os.getenv('DEFAULT_MQ_ADDR', '172.16.0.223')
DEFAULT_MQ_PORT = 5672
DEFAULT_MQ_VHOST = '/'
DEFAULT_MQ_USER = os.getenv('DEFAULT_MQ_USER', 'yz')
DEFAULT_MQ_PWD = os.getenv('DEFAULT_MQ_PWD', 'vuz84B2IkbEtXWF')

### 阿里大鱼 注册
sign_name = '自动化',
template_code = 'SMS_136397944',
try:
    from local_settings import *
except:
    pass

settings = dict(
    debug=debug,
    xsrf_cookies=xsrf_cookies,
    cookie_secret=cookie_secret,
    expire_seconds=expire_seconds,
    sign_name=sign_name,
    template_code=template_code,
    app_name='codo_task_scheduler',
    databases={
        const.DEFAULT_DB_KEY: {
            const.DBHOST_KEY: DEFAULT_DB_DBHOST,
            const.DBPORT_KEY: DEFAULT_DB_DBPORT,
            const.DBUSER_KEY: DEFAULT_DB_DBUSER,
            const.DBPWD_KEY: DEFAULT_DB_DBPWD,
            const.DBNAME_KEY: DEFAULT_DB_DBNAME,
        },
        const.READONLY_DB_KEY: {
            const.DBHOST_KEY: READONLY_DB_DBHOST,
            const.DBPORT_KEY: READONLY_DB_DBPORT,
            const.DBUSER_KEY: READONLY_DB_DBUSER,
            const.DBPWD_KEY: READONLY_DB_DBPWD,
            const.DBNAME_KEY: READONLY_DB_DBNAME,
        }
    },
    redises={
        const.DEFAULT_RD_KEY: {
            const.RD_HOST_KEY: DEFAULT_REDIS_HOST,
            const.RD_PORT_KEY: DEFAULT_REDIS_PORT,
            const.RD_DB_KEY: DEFAULT_REDIS_DB,
            const.RD_AUTH_KEY: DEFAULT_REDIS_AUTH,
            const.RD_CHARSET_KEY: DEFAULT_REDIS_CHARSET,
            const.RD_PASSWORD_KEY: DEFAULT_REDIS_PASSWORD
        }
    },
    mqs={
        const.DEFAULT_MQ_KEY: {
            const.MQ_ADDR: DEFAULT_MQ_ADDR,
            const.MQ_PORT: DEFAULT_MQ_PORT,
            const.MQ_VHOST: DEFAULT_MQ_VHOST,
            const.MQ_USER: DEFAULT_MQ_USER,
            const.MQ_PWD: DEFAULT_MQ_PWD,
        }
    }
)
