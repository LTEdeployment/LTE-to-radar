#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import time
import json
from pymongo import MongoClient
from config import DEBUG_ENV, redis_host, redis_port, redis_db, mongo_uri, mongo_db

REDIS_QUEUE_KEY = 'compute_task_queue'
EMPTY_QUEUE_SLEEP = 5

redisClient = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
mongoClient = MongoClient(mongo_uri)


def handle_task(task):
    pass


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
