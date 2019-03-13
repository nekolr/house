#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from config import configs
from utils.request_utils import get_json
import logging


async def get_proxy_pool():
    """
    获取代理池
    :return:
    """
    # 获取代理服务器地址
    for k, v in configs.proxy.items():
        try:
            pool = await get_json(v)
            if pool is not None and isinstance(pool, list):
                return pool[0]
            else:
                return []
        except BaseException as e:
            logging.error(e)
            # 如果出错使用下一个服务
            continue
