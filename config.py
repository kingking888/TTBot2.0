#coding:utf-8

# ------------ 数据库设置 ------------
#MongoDB数据库设置
MongoDB = {
    'host'          :'127.0.0.1',
    'port'          :27017,
    'database'      :'TTBot',
    'user'          :'',
    'password'      :'',
}

# ------------ 代理设置 ------------
#是否使用代理
PROXY_ENABLE = True
#使用单个的代理ip，优先级最高
#此项若有填写，则使用此代理，后面的不会考虑
# 格式可以为下面几种:
# 1.  "1.1.1.1:1111"
# 2.  "username:password@1.1.1.1:1111"
# 3.  "www.dailiurl.com/path/xxxx"
# 4.  "username:password@www.dailiurl.com/path/xxxx"
PROXY = ''
#IP代理池，优先级低于PROXY高于PROXY_POOL_RAW
# * 建议使用购买的代理池API，一次请求一个代理，每次请求不重复，请求间隔为INTERVAL
# * 或者是一个代理IP文件，文件的一行便是一个代理如:<ip>:<port>
# * 或者是一个代理池IP列表，如:[<ip>:<port>,..]
# 格式可以为下面几种:
# 1、 "http:http://39.108.59.38:8888/Tools/proxyIP.ashx?OrderNumber=xxxx&poolIndex=xxx&cache=1&qty=1"
# 2、 ['1.1.1.1:1111','1.1.1.1:1112','1.1.1.1:1113',...]
# 3、 "D://proxyfile.txt"
PROXY_POOL =  ''


# ------------ 请求设置 ------------
#允许网络请求的HTTP方法
HTTP_METHODS = ['get','head','post','put','options']
# 同步请求的极限重试次数
MAX_REPEATS = 10
#请求失败后的重试次数：
# 0表示不重试；
# >0的表示重试次数
MAX_RETRY = 9
#店铺间的抓取时间间隔:秒
DELAYS = 1
#请求超时时间设置：秒
TIMEOUT = 10
#哪些请求状态码视为正常
OK_CODE = [200,302,0]
# -------------- 日志设置 ----------------
#启用日志
LOG_ENABLE = True
#日志级别
LOG_LEVEL = 'INFO'
#日志文件编码
LOG_FILE_ENCODING = 'UTF-8'
#日志文件路径
LOG_FILE_SAVE_PATH = r'logs/log.txt'
#日志时间格式
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
#日志级别对应格式
LOG_FORMAT = {
    'DEBUG'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'INFO'      : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'WARNING'   : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'ERROR'     : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
    'CRITICAL'  : '%(asctime)s %(name)s(%(levelname)s) - %(message)s',
}
