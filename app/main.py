#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bottle-iot 
@File    ：main.py
@Author  ：Qiuji Chen
@Date    ：2021/10/27 4:32 下午 
"""

import bottle
import routes
import database

app = bottle.default_app()
app.config.load_config('etc/app.conf')

db = database.setup_database(app)
routes.setup_routes(db)


app.run(host=app.config['app.host'], port=app.config['app.port'])
