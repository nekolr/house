#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from requests_html import AsyncHTMLSession
from utils.proxy_pool_utils import get_proxy_pool


class Parser(object):
    """
    解析器基类
    """

    def __init__(self, url):
        self.url = url

    def parse(self):
        """
        解析方法
        :return:
        """
        pass

    @staticmethod
    async def get_request(url):
        """
        静态方法，获取请求
        :param url:
        :return:
        """
        # 获取会话
        session = AsyncHTMLSession()
        # 获取请求
        return await session.get(url)

    @staticmethod
    async def get_request_proxies(url):
        """
        静态方法，通过代理获取请求
        :param url:
        :return:
        """
        # 获取会话
        session = AsyncHTMLSession()
        # 获取代理池
        proxies = await get_proxy_pool()
        # 获取请求
        return await session.get(url, proxies=proxies)
