# -*- coding: utf-8 -*-
"""
http://flask.pocoo.org/docs/config/
"""
import os

DEBUG = True

APP_MODE = 'Development'

APP_SESSION_COOKIE_DOMAIN = '192.168.33.10'

SESSION_COOKIE_NAME = 'sid_dev'
SESSION_COOKIE_DOMAIN = '192.168.33.10'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False
PERMANENT_SESSION_LIFETIME = 7200 * 12

SESSION_KEY_PREFIX = 'session:gameservice:developers:'
SESSION_REDIS_HOST = '192.168.33.10'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = "123456"

#发送群组变更的通知消息到im服务器
REDIS_HOST = "192.168.33.10"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD="123456"

MYSQL_HOST = "192.168.33.10"
MYSQL_PORT = 3306
MYSQL_AUTOCOMMIT = True
MYSQL_CHARSET = 'utf8'
MYSQL_USER = "im"
MYSQL_PASSWD = "123456"
MYSQL_DATABASE = "gobelieve"
# host,port,user,password,db,auto_commit,charset
MYSQL = (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, MYSQL_DATABASE, MYSQL_AUTOCOMMIT, MYSQL_CHARSET)

# mail
MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_USERNAME = 'webmaster@gobelieve.io'
MAIL_PASSWORD = 'gbpassw0rd'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_DEFAULT_SENDER = 'webmaster@gobelieve.io'
MAIL_DEBUG = True
MAIL_SUPPRESS_SEND = False


#微信
APP_ID = 'wxa5ed698cbbfe36e0'
APP_SECRET = 'cd8c074afcb83815a9d0f278bfadf30b'

KEFU_APPID = 1453

#robotd
RPC = "http://127.0.0.1:60003"

IM_RPC_URL = "http://192.168.33.1:6666"
IM_URL = "http://192.168.33.10"

FS_HOST="192.168.33.10"
FS_PORT=8083

#微信第三方平台的appid
WX_COMPONENT_APPID = "wx8ec7ea1fab1fbbf2"
WX_COMPONENT_APPSECRET = "a27fb4d3ee36978b5288df1843a29c88"
WX_TOKEN = '__aimeitu__'
WX_ENCODING_AES_KEY = "SlPk3YEvdcWUAE2BbCfX78tokYo8nyCQ4dk5KKBU1vu"

