#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from requests_html import AsyncHTMLSession
from analyzer.lian_jia import LianJia


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
    # get_html('https://bj.lianjia.com/ershoufang')


if __name__ == '__main__':
    start()

