#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis, time, json
import scipy.io as scio
from pymongo import MongoClient
from Lumped_Power import exe_main

# read config
with open('../config/default.json') as config_file:
    config = json.load(config_file)

# init redis & mongo
redisClient = redis.StrictRedis(host = config['redis_host'], port = config['redis_port'], db = config['redis_db'])
mongoClient = MongoClient(config['mongo_uri'])

def handle_task(task):
    lte_direction = []
    lte_direction = []
    lte_direction = []
    print task
    print exe_main(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0,
             0, 0, 0, 0, 0,
             0,
             lte_direction, lte_direction, lte_direction, 0, 0,
             0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0)

def log_print(message):
    if (config['DEBUG_ENV']):
        print message

# loop
while(True):
    # task = redisClient.lpop(config['redis_task_lte_queue'])
    task = redisClient.lindex(config['redis_task_lte_queue'], 0)
    if (not task):
        log_print('queue is empty')
        time.sleep(config['queue_empty_sleep_time'])
        continue
    handle_task(json.loads(task))
    time.sleep(config['queue_empty_sleep_time'])
