#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import redis
import time
import json
from pymongo import MongoClient
from Lumped_Power import exe_main

# read config
with open('../config/default.json') as config_file:
  config = json.load(config_file)

# init redis & mongo
redis_client = redis.StrictRedis(host=config['redis_host'], port=config[
                                 'redis_port'], db=config['redis_db'])
mongo_client = MongoClient(config['mongo_uri'])
direction_collections = mongo_client[config['mongo_db']]['directions']
task_collections = mongo_client[config['mongo_db']]['tasks']


def num(s):
  try:
    return int(s)
  except ValueError:
    return float(s)


def get_direction(direction_name):
  direction = direction_collections.find_one({'name': direction_name})
  if (direction == None):
    log_print('direction %s not found!' % direction_name)
    return None
  if (direction['data'] == None):
    log_print('direction ' + direction_name + 'not ready yet!')
    return None
  return direction['data']


def get_sub_bundle(bundle, name):
  sub_bundle = bundle[name]

  def foobar(key):
    return num(sub_bundle[key])
  return foobar


def handle_task(task):
  print(task)
  bundle = task['bundle']
  lteDirection = get_direction(bundle['lteDirection'])
  userDirection = get_direction(bundle['userDirection'])
  radarDirection = get_direction(bundle['radarDirection'])
  for item in [lteDirection, userDirection, radarDirection]:
    if item == None:
      return
  pub = get_sub_bundle(bundle, 'pub')
  lte = get_sub_bundle(bundle, 'lte')
  user = get_sub_bundle(bundle, 'user')
  radar = get_sub_bundle(bundle, 'radar')
  result = exe_main(pub('acir_min'), pub('acir_max'), pub('acir_space'), pub('antenna_flag'),
                    pub('lte_min_d'), pub('sR'), pub('lR'), lte('lte_power'),
                    lte('lte_antenna_height'), lte('lte_frequency'),
                    user('user_antenna_height'), user('user_frequency'), lte('lte_bindwidth'),
                    radar('radar_antenna_height'), lte('lte_antenna_gain'), user('user_antenna_gain'),
                    radar('radar_antenna_gain'), lte('lte_antenna_loss_factor'), user('user_loss_factor'),
                    radar('radar_loss_factor'), radar('radar_bindwidth'), lteDirection, userDirection, radarDirection,
                    pub('environment1'), pub('environment2'), radar('radar_antenna_tilt'), pub('branch'),
                    pub('resource_block'), lte('lte_feederline_factor'), radar('radar_feeder_loss'), lte('lte_noise_figure'),
                    user('user_noise_figure'), radar('radar_noise_figure'), pub('uti_or_multi'), pub('compensation_factor'), pub('transpmax'), 1)


def log_print(message):
  if (config['DEBUG_ENV']):
    print message

# loop
while(True):
  # task = redis_client.lpop(config['redis_task_lte_queue'])
  task = redis_client.lindex(config['redis_task_lte_queue'], 0)
  if (not task):
    log_print('queue is empty')
    time.sleep(config['queue_empty_sleep_time'])
    continue
  handle_task(json.loads(task))
  if (config['DEBUG_ENV']):
    time.sleep(config['queue_empty_sleep_time'])
