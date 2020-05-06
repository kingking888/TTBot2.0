#coding:utf-8

import requests
from config import *
from sync_proxy import get_proxy
from log import getLogger

logger = getLogger(__name__)

def send_request(method,
                 url,
                 session=None,
                 JSON=False,
                 retries=MAX_RETRY,
                **kwargs):
    if method.lower() not in HTTP_METHODS:
        raise Exception(f'非法请求操作:{method}.')
    if session is None:
        session = requests.session()
    if retries == -1:
        attempt = -1
    elif retries == 0:
        attempt = 1
    else:
        attempt = retries + 1
    while attempt != 0:
        try:
            response = session.request(method,url,**kwargs)
            code = response.status_code
        except Exception as e:
            logger.error(f'[请求异常]{e.__class__.__name__}:{e}')
            kwargs['proxies'] = get_proxy()
            attempt -= 1
            continue
        if code not in OK_CODE :
            logger.error(f'[{code}]非正常请求页面.使用代理重试中.')
            kwargs['proxies'] = get_proxy()
            attempt -= 1
            continue
        if JSON:
            try:
                response = response.json()
                code = response.get('code')
                shopRecordBeanList = response.get('shopRecordBeanList')
                if code and code not in OK_CODE or not shopRecordBeanList:
                    raise Exception(f'[{code}]需要验证码')
            except Exception as e:
                logger.error(f'[无效json格式]{e.__class__.__name__}:{e}')
                kwargs['proxies'] = get_proxy()
                attempt -= 1
                continue
        return response

