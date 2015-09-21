# -*- coding: utf-8 -*-
from bouser_db import interfaces, service
from bouser_db import service

__author__ = 'mmalkov'


def make(config):
    return service.DataBaseService(config)