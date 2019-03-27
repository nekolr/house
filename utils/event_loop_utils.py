#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio


def put_tasks(tasks, args=None):
    """
    将任务放入事件循环（一个任务至多允许使用一个参数）
    :param tasks: 任务集合
    :param args: 任务执行需要的参数集合
    :return: 任务的执行结果
    """
    loop = asyncio.get_event_loop()
    if args is not None:
        tasks = [
            asyncio.ensure_future(task(arg)) for task, arg in zip(tasks, args)
        ]
    else:
        tasks = [
            asyncio.ensure_future(task()) for task in tasks
        ]
    # _ 是用来过滤掉最后一个元素
    results, _ = loop.run_until_complete(asyncio.wait(tasks))
    return [r.result() for r in results]


def close_event_loop():
    """
    关闭事件循环
    :return:
    """
    loop = asyncio.get_event_loop()
    loop.close()
