#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class House(object):
    def __init__(self):
        # 数据来源
        self.origin = ""
        # 名称（发布标题）
        self.houseName = ""
        # 区域名称
        self.houseArea = ""
        # 地理位置
        self.houseLocation = ""
        # 链接
        self.houseLink = ""
        # 图片（第一张）
        self.houseImage = ""
        # 所在楼层
        self.houseFloor = ""
        # 建筑面积
        self.buildingArea = ""
        # 套内面积
        self.innerArea = ""
        # 户型
        self.housePlan = ""
        # 朝向
        self.houseTowards = ""
        # 单价
        self.unitPrice = ""
        # 总价
        self.totalPrice = ""
        # 产权年限
        self.houseProperty = ""
        # 交易权属
        self.tradingRight = ""
        # 装修情况
        self.decoration = ""
        # 房屋介绍
        self.description = ""
        # 标签
        self.tags = []

    def __str__(self):
        return '数据来源：%s 名称：%s 区域名称：%s 地理位置：%s 链接：%s 图片：%s ' \
               '所在楼层：%s 建筑面积：%s 套内面积：%s 户型：%s 朝向：%s ' \
               '单价：%s 总价：%s 产权年限：%s 交易权属：%s 装修情况：%s 房屋介绍：%s' % \
               (self.origin, self.houseName, self.houseArea, self.houseLocation,
                self.houseLink, self.houseImage, self.houseFloor,
                self.buildingArea, self.innerArea, self.housePlan,
                self.houseTowards, self.unitPrice, self.totalPrice,
                self.houseProperty, self.tradingRight, self.decoration, self.description)
