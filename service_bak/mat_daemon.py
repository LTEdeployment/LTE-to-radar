#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import scio
import time

REDIS_QUEUE_KEY = 'task_queue'
EMPTY_QUEUE_SLEEP = 5
client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

def read_mat(file_path):
    data = scio.loadmat(file_path)
    for key in data:
        if (key != '__globals__') and (key != '__header__') and (key != '__version__'):
            return data[key]
    return 0

def handle_task(directions_task):
    directions = read_mat(directions_task.file_path)
    client.set('directions_' + directions_task.name, directions)

def log_print(message):
    print message

while(True):
    task = client.rpop(REDIS_QUEUE_KEY)
    if (not task):
        log_print('queue is empty')
        time.sleep(EMPTY_QUEUE_SLEEP)
        continue
    handle_task(task)

