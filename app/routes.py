#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bottle-iot 
@File    ：routes.py
@Author  ：Qiuji Chen
@Date    ：2021/11/12 3:34 下午 
"""

import model
import joblib
import datetime
from json import dumps
from bson import json_util
from scipy.stats.stats import mode
from bottle import Response, get, post, error, route, request, static_file


def setup_routes(db):
    col = db['air']

    @get('/air/list')
    def get_room_air():
        page = int(request.query.page) or 1
        size = int(request.query.limit) or 10

        result = list(col.find({}).limit(size).skip((page - 1) * size))
        return dumps(result, default=json_util.default)

    @post('/air/create')
    def create_record():
        data = request.json

        col.insert_one(data)
        return {"success": True}

    @get('/air/forecast')
    def forecast_air():
        r = model.get_model(db)
        # read the save model
        m = joblib.load('model.pkl')
        # forecast
        preds = m.predict(r[1])
        dates = []
        all_pm2 = []
        all_pm10 = []
        all_o3 = []
        all_no2 = []
        all_so2 = []
        all_co = []
        for i in range(1, 9):
            item = preds[i]
            today = datetime.datetime.now()
            date = (today + datetime.timedelta(days=i)).date()
            dates.append(str(date))
            all_pm2.append(item[0])
            all_pm10.append(item[1])
            all_o3.append(item[2])
            all_no2.append(item[3])
            all_so2.append(item[4])
            all_co.append(item[5])
        
        result = {"dates": dates, "all_pm2": all_pm2, "all_pm10": all_pm10,
                  "all_o3": all_o3, "all_no2": all_no2, "all_so2": all_so2, "all_co": all_co}
        return result

    @route('/static/<path>')
    def server_static(path):
        return static_file(path, root=r"web/")

    @error(404)
    def error404(err):
        print(err)
        return '404 - the requested page could not be found'
