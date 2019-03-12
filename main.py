#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from resolver.lianjia import LianJiaParser
from dao.house_dao import save_house


def run_task(origin, parser):
    """
    执行任务
    :param origin: 数据来源
    :param parser: 解析器
    :return:
    """
    models = parser.parse()
    for model in models:
        save_house(origin, model)


def start():
    """
    爬虫入口
    :return:
    """
    run_task('链家', LianJiaParser('https://bj.lianjia.com/ershoufang/'))


if __name__ == '__main__':
    start()
