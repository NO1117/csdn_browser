#!/usr/bin/env/ python 
# -*- coding:utf-8 -*-
# Author:Mr.Xu


MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'Sale_58'
MONGO_PASSWORD = None

# API 配置
API_HOST = '127.0.0.1'
API_PORT = 5000

READ_NUM = 1000
TASK_NUM = 500

REFER_LIST=[
            {'http://blog.csdn.net/dala_da/article/details/79401163'},
            {'http://blog.csdn.net/'},
            {'https://www.sogou.com/tx?query=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F&hdq=sogou-site-706608cfdbcc1886-0001&ekv=2&ie=utf8&cid=qb7.zhuye&'},
            {'https://www.baidu.com/s?tn=98074231_1_hao_pg&word=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F'},
            {'https://www.baidu.com/link?url=N5tv6Q8HFZKoiM0jwgasxeZFcACmTQj6ZdhGH_9tw-4moasBNbt1ziUg7Hc3yrNdDUzkywJWaptTv2nB7Mhn6Zmmbbcb73KDiV9UkkyiLIi&wd=&eqid=b01ced82000163f1000000025bc6f2c2'},
        ]