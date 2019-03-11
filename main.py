#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from analyzer.lianjia import LianJiaParser


def run_task(parser):
    """
    执行任务
    :param parser: 解析器
    :return:
    """
    parser.parse()


def start():
    """
    爬虫入口
    :return:
    """
    run_task(LianJiaParser('https://bj.lianjia.com/ershoufang/'))


if __name__ == '__main__':
    start()
