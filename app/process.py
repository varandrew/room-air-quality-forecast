#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：bottle-iot 
@File    ：database.py
@Author  ：Qiuji Chen
@Date    ：2021/11/12 3:47 下午 
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


def process_data(db):
    col = db["air"]
    data = [[0 if v == '' else v for v in list(
        item.values())[1:]] for item in list(col.find({}, {"_id": 0}))]
    train_data = np.array_split(data, 3)
    X = pd.DataFrame(train_data[1])
    y = pd.DataFrame(train_data[2])
    X_test = pd.DataFrame(train_data[0])
    my_imputer = SimpleImputer()
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, train_size=0.8, test_size=0.2, random_state=0)
    imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
    imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
    imputed_X_train.columns = X_train.columns
    imputed_X_valid.columns = X_valid.columns
    imputed_y_train = pd.DataFrame(my_imputer.fit_transform(y_train))
    imputed_y_valid = pd.DataFrame(my_imputer.transform(y_valid))
    imputed_y_train.columns = y_train.columns
    imputed_y_valid.columns = y_valid.columns
    imputed_X_test = pd.DataFrame(my_imputer.fit_transform(X_test))

    results = [imputed_X_train, imputed_X_valid,
               imputed_y_train, imputed_y_valid, imputed_X_test]
    return results
