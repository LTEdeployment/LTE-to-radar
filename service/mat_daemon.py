#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis, time, json
import scipy.io as scio
from pymongo import MongoClient
from config import DEBUG_ENV, redis_host, redis_port, redis_db, mongo_uri, mongo_db

REDIS_QUEUE_KEY = 'directions_task_queue'
EMPTY_QUEUE_SLEEP = 5

redisClient = redis.StrictRedis(host = redis_host, port=redis_port, db=redis_db)
mongoClient = MongoClient(mongo_uri)

def read_mat(file_path):
    data = scio.loadmat(file_path)
    for key in data:
        if (key != '__globals__') and (key != '__header__') and (key != '__version__'):
            return data[key]
    return 0

def handle_task(directions_task):
    file_path = '../uploads/' + directions_task['file']['filename']
    directions = read_mat(file_path)
    collections = mongoClient[mongo_db]['directions']
    direction = collections.find_one({'name': directions_task['name']})
    direction['data'] = directions.tolist()
    collections.save(direction)
    log_print('direction update: ' + directions_task['name'])

def log_print(message):
    if (DEBUG_ENV):
        print message

while(True):
    task = redisClient.rpop(REDIS_QUEUE_KEY)
    if (not task):
        log_print('queue is empty')
        time.sleep(EMPTY_QUEUE_SLEEP)
        continue
    handle_task(json.loads(task))
    time.sleep(EMPTY_QUEUE_SLEEP)

