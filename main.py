#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from resolver.lianjia import LianJiaParser
from dao.house_dao import save_house
from utils.event_loop_utils import put_tasks
from utils.mysql_utils import init


def run_task(parser):
    """
    执行任务
    :param parser: 解析器
    :return:
    """
    models = parser.parse()
    for model in models:
        put_tasks([save_house], [model])


def start():
    """
    爬虫入口
    :return:
    """
    put_tasks([init])
    # run_task(LianJiaParser('https://bj.lianjia.com/ershoufang/'))
    run_task(LianJiaParser('https://bj.lianjia.com/ershoufang/tongzhou/'))


if __name__ == '__main__':
    start()
