#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis, time, json
import scipy.io as scio
from pymongo import MongoClient

# read config
with open('../config/default.json') as config_file:
    config = json.load(config_file)

# init redis & mongo
redisClient = redis.StrictRedis(host = config['redis_host'], port = config['redis_port'], db = config['redis_db'])
mongoClient = MongoClient(config['mongo_uri'])

def read_mat(file_path):
    data = scio.loadmat(file_path)
    for key in data:
        if (key != '__globals__') and (key != '__header__') and (key != '__version__'):
            return data[key]
    return False

def handle_task(directions_task):
    file_path = '../uploads/' + directions_task['file']['filename']
    directions = read_mat(file_path)
    collections = mongoClient[config['mongo_db']]['directions']
    direction = collections.find_one({'name': directions_task['name']})
    if direction == None:
        log_print('direction update failed: ' + directions_task['name'])
        return
    direction['data'] = directions.tolist()
    direction['is_resolved'] = True
    collections.save(direction)
    log_print('direction update: ' + directions_task['name'])

def log_print(message):
    if (config['DEBUG_ENV']):
        print message

# loop
while(True):
    task = redisClient.rpop(config['redis_mat_directions_queue'])
    # task = redisClient.lindex(config['redis_mat_directions_queue'], 0)
    if (not task):
        log_print('queue is empty')
        time.sleep(config['queue_empty_sleep_time'])
        continue
    handle_task(json.loads(task))
    time.sleep(config['queue_empty_sleep_time'])
