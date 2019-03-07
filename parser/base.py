#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def parse(self):
        pass

