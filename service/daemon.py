# -*- coding: utf-8 -*-
import redis
import time
from Lumped_Power import *

print judge_affect(1,
             2, 3, 4, 5, 6,
             2, 3, 4, 5, 6,
             2, 3, 4, 5, 6,
             2, 3, 4, 5, 6,
             2, 3, 4, 5, 6,
             2, 3, 4, 5, 6)
exit(1)

def handle_task(task):
    log_print(task)
    judge_affect(task)
    time.sleep(5)
    pass

def log_print(message):
    print message

REDIS_QUEUE_KEY = 'task_queue'
EMPTY_QUEUE_SLEEP = 5
client = redis.StrictRedis(host='115.159.85.182', port=6379, db=0)

while(True):
    task = client.rpop(REDIS_QUEUE_KEY)
    if (not task):
        log_print('queue is empty')
        time.sleep(EMPTY_QUEUE_SLEEP)
        continue
    handle_task(task)
