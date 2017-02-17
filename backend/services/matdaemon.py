#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import time, json
import scipy.io as scio
from logbook import Logger, TimedRotatingFileHandler
from config import config
from redis_client import redis_client
from mongo_client import direction_collections

logger = Logger('matdaemon')
handler = TimedRotatingFileHandler('/tmp/logs', date_format="%Y%m%d")
# logger.handlers.append(handler)
handler.push_application()

def read_mat(file_path):
    data = scio.loadmat(file_path)
    for key in data:
        if (key != '__globals__') and (key != '__header__') and (key != '__version__'):
            return data[key]
    return False

def handle_task(directions_task):
    file_path = '../uploads/' + directions_task['file']['filename']
    directions = read_mat(file_path)
    direction = direction_collections.find_one({'name': directions_task['name']})
    if direction == None:
        log_print('direction update failed: %s' % directions_task['name'])
        return
    direction['data'] = directions.tolist()
    direction['finished'] = True
    direction_collections.save(direction)
    log_print('direction update: %s' % directions_task['name'])

def log_print(message):
    if config['DEBUG_ENV']:
        print(message)
    logger.info(message)

# loop
while(True):
    task = redis_client.rpop(config['redis_mat_directions_queue'])
    # task = redis_client.lindex(config['redis_mat_directions_queue'], 0)
    if not task:
        log_print('queue is empty')
        if config['DEBUG_ENV']:
            time.sleep(config['queue_empty_sleep_time'])
        continue
    handle_task(json.loads(task))
    if config['DEBUG_ENV']:
        time.sleep(config['queue_empty_sleep_time'])
