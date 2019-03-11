#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from requests_html import AsyncHTMLSession


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
