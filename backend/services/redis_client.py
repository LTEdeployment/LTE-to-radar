# -*- coding: utf-8 -*-
import redis
from config import config

redis_client = redis.StrictRedis(host = config['redis_host'], port = config['redis_port'], db = config['redis_db'], password = config['redis_password'])
