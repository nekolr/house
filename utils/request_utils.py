#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import aiohttp


async def _fetch_json(session, url):
    """
    获取响应数据
    :param session:
    :param url:
    :return:
    """
    async with session.get(url, timeout=6) as response:
        return await response.json()


async def get_json(url):
    """
    通过 get 方法请求 url
    :param url:
    :return:
    """
    async with aiohttp.ClientSession() as session:
        return await _fetch_json(session, url)
