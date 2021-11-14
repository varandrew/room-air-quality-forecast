#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bottle-iot 
@File    ：database.py
@Author  ：Qiuji Chen
@Date    ：2021/11/12 3:47 下午 
"""
from sklearn.ensemble import RandomForestRegressor # 随机树森林模型
import joblib # 保存模型为pkl
from sklearn.metrics import mean_absolute_error # MAE评估方法
from process import process_data # 取数据

def get_model(db, name="model.pkl"):
    """
    :param name: 模型文件名
    :return:
        [socre: MAE评估结果,
        X_test: 预测数据集]
    """
    # 取到数据
    [X_train, X_valid, y_train, y_valid, X_test] = process_data(db)
    # 随机树森林模型
    model = RandomForestRegressor(random_state=0, n_estimators=1001)
    # 训练模型
    model.fit(X_train, y_train)
    # 预测模型，用上个星期的数据
    preds = model.predict(X_valid)
    # 用MAE评估
    score = mean_absolute_error(y_valid, preds)
    # 保存模型到本地
    joblib.dump(model, name)
    # 返回MAE
    return [score, X_test]