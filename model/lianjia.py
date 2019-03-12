#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .base import House


class LianJia(House):
    def __init__(self):
        super().__init__()
        # 每个实体维护的一份映射，方便在爬取到数据后封装到实体中
        self.mapping = {
            '房屋户型': 'housePlan',
            '所在楼层': 'houseFloor',
            '建筑面积': 'buildingArea',
            '套内面积': 'innerArea',
            '房屋朝向': 'houseTowards',
            '装修情况': 'decoration',
            '产权年限': 'houseProperty',
            '交易权属': 'tradingRight'
        }
