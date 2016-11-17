import redis
import time

REDIS_QUEUE_KEY = 'lte_comput_queue'
EMPTY_QUEUE_SLEEP = 1
client = redis.StrictRedis(host='localhost', port=6379, db=0)

while(True):
    task = client.rpop(REDIS_QUEUE_KEY)
    if (not task):
        print 'empty!'
        time.sleep(EMPTY_QUEUE_SLEEP)
        continue
    pass
