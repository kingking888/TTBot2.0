#coding:utf-8

from settings import HOSTS,SUIT,COMMENT_HOSTS,SEC_HOSTS,SEC_SUIT
from log import getLogger

logger = getLogger(__name__)

class TTApi:

    def __init__(self,version:int=700):
        self.register(version)

    def register(self,version:int):
        mathed = 0
        if version in HOSTS:
            host = HOSTS[version]
            for _range in SUIT.keys():
                if _range[0]<= version <= _range[1]:
                    suit = SUIT[_range]
                    for k in suit:
                        if k == 'VIDEO_COMMENTS':
                            setattr(self,k,COMMENT_HOSTS[version]+suit[k])
                        else:
                            setattr(self,k,host + suit[k])
                        logger.info(f'[version {version}] {k} API inited.')
            mathed = 1
        if version in SEC_HOSTS:
            host = SEC_HOSTS[version]
            for _range in SEC_SUIT.keys():
                if _range[0]<= version <= _range[1]:
                    suit = SEC_SUIT[_range]
                    for k in suit:
                        setattr(self, k, host + suit[k])
                        logger.info(f'[version {version}] {k} API inited.')
            mathed = 1
        if not mathed:
            logger.error(f'No API version matched (got version {version}).Check another version of the App.')
