#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from config_default import configs


class Dict(dict):
    """
    Simple dict but support access as x.y style.
    """

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def to_dict(d):
    """
    转成自定义的字典类型
    :param d:
    :return:
    """
    dic = Dict()
    for k, v in d.items():
        dic[k] = to_dict(v) if isinstance(v, dict) else v
    return dic


# 将配置转成自定义的字典类型
configs = to_dict(configs)
