#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio


def put_event_loop(tasks, urls):
    """
    将任务放入时间循环
    :param tasks: 任务集合
    :param urls: 任务的请求地址集合
    :return: 任务的执行结果
    """
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(task(url)) for task, url in zip(tasks, urls)
    ]
    # _ 是用来过滤掉最后一个元素
    results, _ = loop.run_until_complete(asyncio.wait(tasks))
    return [r.result() for r in results]


def close_event_loop():
    """
    关闭时间循环
    :return:
    """
    loop = asyncio.get_event_loop()
    loop.close()
