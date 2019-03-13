#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.mysql_utils import *
import time
import warnings


async def save_house(house):
    # 生成表名
    table_name = "T" + time.strftime('%Y%m%d', time.localtime(time.time()))

    create_table_sql = """CREATE TABLE IF NOT EXISTS %s (
        id int auto_increment primary key,
        origin varchar(255),
        houseName varchar(255),
        houseArea varchar(255),
        houseLocation varchar(255),
        houseLink varchar(255),
        houseImage varchar(255),
        houseFloor varchar(255),
        buildingArea varchar(255),
        innerArea varchar(255),
        housePlan varchar(255),
        houseTowards varchar(255),
        unitPrice varchar(255),
        totalPrice varchar(255),
        houseProperty varchar(255),
        tradingRight varchar(255),
        decoration varchar(255),
        description varchar(255),
        tags varchar(255)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""" % table_name

    # 忽略表已经存在的警告
    warnings.filterwarnings('ignore')
    # 执行 SQL
    count = await execute(create_table_sql)

    insert_sql = """INSERT INTO %s (origin, houseName, houseArea, houseLocation, houseLink, 
    houseImage, houseFloor, buildingArea, innerArea, housePlan, houseTowards, unitPrice, 
    totalPrice, houseProperty, tradingRight, decoration, description, tags) VALUES 
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""" % table_name

    count = await execute(insert_sql, [house.origin, house.houseName, house.houseArea, house.houseLocation,
                                       house.houseLink, house.houseImage, house.houseFloor, house.buildingArea,
                                       house.innerArea, house.housePlan, house.houseTowards, house.unitPrice,
                                       house.totalPrice, house.houseProperty, house.tradingRight, house.decoration,
                                       house.description, house.tags])
