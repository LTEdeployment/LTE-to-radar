'use strict';

const tool = require('../core/tool');
const Task = require('../models/task');
const app = require('../core/app');
const cache = require('../core/cache');
let pub = {};

pub.create = async(req, res) => {
  let parcel = req.body.parcel;
  let task = new Task(JSON.parse(parcel));
  task.save(function (err, ops) {
    // 保存失败了
    if (err) {
      tool.l(err);
      res.status(500);
      return;
    }
    if (!ops) {
      res.status(501);
      return;
    }

    // 往 redis 队列中添加一个任务
    cache.lpush(ops);

    // 给管理员发送邮件
    res.mailer.send('email', {
      to: 'xhinliang@gmail.com',
      subject: `新的任务`,
      description: JSON.stringify(ops)
    }, function (err) {
      if (err) {
        tool.debug('send email error: ' + err);
        return;
      }
      tool.debug('send email success !');
    });

    // 原样返回
    res.send(JSON.stringify(ops));
  })
};

module.exports = pub;
