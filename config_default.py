#!/usr/bin/env python3
# -*- coding: utf-8 -*-
configs = {
    'app': {
        # 是否需要代理池
        'require_proxy': True
    },
    'db': {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'house',
        'charset': 'utf8',
        'autocommit': True,
        'maxsize': 10,
        'minsize': 1
    },
    # 代理池服务地址
    # https://github.com/jhao104/proxy_pool
    # https://github.com/chenjiandongx/async-proxy-pool
    'proxy': {
        # 'server_a': 'http://localhost:5010/get_all',
        'server_b': 'http://localhost:3289/get/10'
    }
}
