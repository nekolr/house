#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .base import Parser
from utils.event_loop_utils import put_event_loop
from model.lianjia import LianJia


class LianJiaParser(Parser):
    """
    链家解析器
    """

    def __init__(self, url):
        super().__init__(url)
        # 是否需要下钻获取详细信息
        self.requireDetail = True

    def parse(self):
        results = put_event_loop([Parser.get_request], [self.url])
        for result in results:
            lis = _get_list(result.html)
            for li in lis:
                if _filter_useless(li):
                    model = LianJia()
                    _get_outside(li, model)
                    # 下钻详情页
                    if self.requireDetail:
                        _get_detail(model.houseLink, model)


def _get_list(html):
    """
    获取列表
    :return:
    """
    return html.find('.sellListContent>li')


def _filter_useless(one):
    """
    过滤无用的发布信息（广告）
    :param one: 一条房源
    :return:
    """
    if one.attrs.get('class')[0] != 'list_app_daoliu':
        return True
    else:
        return False


def _get_outside(one, model):
    """
    获取外部信息
    :param one: 一条房源
    :return:
    """
    # 房源发布的头部信息
    post_title = one.find('div.info.clear div.title a', first=True)
    house_name = post_title.text
    house_link = post_title.attrs.get('href')

    # 地址信息等
    house_location = one.find('div.info.clear div.address div.houseInfo a', first=True).text

    # 所在区域信息等
    house_area = one.find('div.info.clear div.flood div.positionInfo a', first=True).text

    # 价格信息等
    post_price = one.find('div.info.clear div.followInfo div.priceInfo', first=True)
    house_total_price = post_price.find('div.totalPrice span', first=True).text
    house_unit_price = post_price.find('div.unitPrice span', first=True).text

    model.houseName = house_name
    model.houseLink = house_link
    model.houseLocation = house_location
    model.houseArea = house_area
    model.totalPrice = house_total_price
    model.unitPrice = house_unit_price


def _get_detail(url, model):
    """
    获取详情信息
    :param url: 详情页地址
    :param model: 实体
    :return:
    """
    results = put_event_loop([Parser.get_request], [url])
    for result in results:
        html = result.html
        d = dict()
        lis = html.find('#introduction div div.introContent div.base div.content ul > li')
        for li in lis:
            # 详细信息
            item = li.text
            # 属性名称
            prop_name = item[:4]
            prop_value = item[4:]
            d[prop_name] = prop_value
