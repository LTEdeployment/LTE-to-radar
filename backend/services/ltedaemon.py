#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import time
import json
from Lumped_Power import exe_main
from config import config
from redis_client import redis_client
from mongo_client import direction_collections, task_collections

# 将一个字符串转换为一个整型或者浮点型数据
def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def get_direction(direction_name):
    direction = direction_collections.find_one({'name': direction_name})
    if direction == None:
        log_print('direction %s not found!' % direction_name)
        return None
    if direction['data'] == None:
        log_print('direction ' + direction_name + 'not ready yet!')
        return None
    return direction['data']

def get_sub_bundle(bundle, name):
    sub_bundle = bundle[name]
    def foobar(key):
        try:
            return num(sub_bundle[key])
        except KeyError:
            print 'key not found %s' % key
            return 0
    return foobar

def handle_task(task):
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
    task_item = task_collections.find_one({'name': task['name']})
    if task_item == None:
        log_print('can not find task in db!')
        return
    task_item['result'] = []
    result = exe_main(pub('acir_min'), pub('acir_max'), pub('acir_space'), pub('antenna_flag'),
                      pub('lte_min_d'), pub('sR'), pub('lR'), lte('lte_power'),
                      lte('lte_antenna_height'), lte('lte_frequency'),
                      user('user_antenna_height'), user('user_frequency'), lte('lte_bindwidth'),
                      radar('radar_antenna_height'), lte('lte_antenna_gain'), user('user_antenna_gain'),
                      radar('radar_antenna_gain'), lte('lte_antenna_loss_factor'), user('user_loss_factor'),
                      radar('radar_loss_factor'), radar('radar_bindwidth'), lteDirection, userDirection, radarDirection,
                      pub('environment1'), pub('environment2'), radar('radar_antenna_tilt'), pub('branch'),
                      pub('resource_block'), lte('lte_feederline_factor'), radar('radar_feeder_loss'), lte('lte_noise_figure'),
                      user('user_noise_figure'), radar('radar_noise_figure'), pub('uti_or_multi'), pub('compensation_factor'), pub('transpmax'), 6)
    for item in result:
        print 'result: %f' % item
        task_item['result'].append(item)
        task_collections.save(task_item)
    task_item['finished'] = True
    task_collections.save(task_item)

def log_print(message):
    if config['DEBUG_ENV']:
      print message

# loop
while(True):
    task = redis_client.rpop(config['redis_task_lte_queue'])
    # task = redis_client.lindex(config['redis_task_lte_queue'], 0)
    if not task:
        log_print('queue is empty')
        time.sleep(config['queue_empty_sleep_time'])
        continue
    log_print(task)
    handle_task(json.loads(task))
    if config['DEBUG_ENV']:
        time.sleep(config['queue_empty_sleep_time'])
