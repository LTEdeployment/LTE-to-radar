# -*- coding: utf-8 -*-
from config import config
from pymongo import MongoClient

mongo_client = MongoClient(config['mongo_uri'])
direction_collections = mongo_client[config['mongo_db']]['directions']
task_collections = mongo_client[config['mongo_db']]['tasks']
