#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bottle-iot 
@File    ：database.py
@Author  ：Qiuji Chen
@Date    ：2021/11/12 3:47 下午 
"""
import pymongo


def setup_database(app):
    uri = app.config['mongo.uri']
    client = pymongo.MongoClient(uri)
    db = client[app.config['mongo.db_name']]
    return db
