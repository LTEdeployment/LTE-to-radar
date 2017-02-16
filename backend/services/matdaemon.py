#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import redis, time, json
import scipy.io as scio
from pymongo import MongoClient
from logbook import Logger, TimedRotatingFileHandler

# read config
with open('../config/default.json') as config_file:
    config = json.load(config_file)

# init redis & mongo
redis_client = redis.StrictRedis(host = config['redis_host'], port = config['redis_port'], db = config['redis_db'])
mongo_client = MongoClient(config['mongo_uri'])
collections = mongo_client[config['mongo_db']]['directions']

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
    direction = collections.find_one({'name': directions_task['name']})
    if direction == None:
        log_print('direction update failed: %s' % directions_task['name'])
        return
    direction['data'] = directions.tolist()
    direction['finished'] = True
    collections.save(direction)
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
