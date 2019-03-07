#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from requests_html import AsyncHTMLSession


def get_html(url):
    # 启动
    session = AsyncHTMLSession()
    # 获取请求
    return session.get(url)


def start():
    """
    爬虫入口
    :return:
    """


if __name__ == '__main__':
    start()

