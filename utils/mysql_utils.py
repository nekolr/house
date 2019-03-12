#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import aiomysql
import logging
from config import configs


async def init():
    """
    初始化线程池
    :return:
    """
    await create_pool(loop=None, **configs.db)


async def create_pool(loop=None, **kwargs):
    """
    创建数据库连接池
    :param loop: event loop
    :param kwargs: 连接池配置参数
    :return:
    """
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kwargs.get('host', 'localhost'),
        port=kwargs.get('port', 3306),
        user=kwargs.get('user'),
        password=kwargs.get('password'),
        db=kwargs.get('db'),
        charset=kwargs.get('charset', 'utf8'),
        autocommit=kwargs.get('autocommit', True),
        maxsize=kwargs.get('maxsize', 10),
        minsize=kwargs.get('minsize', 1),
        loop=loop
    )


async def select(sql, args, size=None):
    """
    执行查询操作
    :param sql: 查询 SQL
    :param args: 查询参数
    :param size: 查询返回结果数量
    :return: 结果集
    """
    logging.info('SQL: %s' % sql)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs


async def execute(sql, args, autocommit=True):
    """
    执行插入、删除和更新操作
    :param sql: SQL 语句
    :param args: 参数
    :param autocommit 是否自动提交
    :return: 受影响的行数
    """
    logging.info('SQL: %s' % sql)
    global __pool
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args or ())
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise e
        return affected
