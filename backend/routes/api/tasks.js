const router = require('express').Router();
const TaskModel = require('../../models/tasks');
const check = require('../../middlewares/apicheck');
const cache = require('../../lib/cache');

const TASK_QUEUE_NAME = 'task_queue';

// 根据任务 ID 查询指定的任务
router.get('/id/:id', check.checkNotLogin, function(req, res, next) {
  let author = req.session.user._id;
  let id = req.params.id;
  TaskModel
    .getTaskById(id)
    .then(function(result) {
      let task = result[0];
      res.send(JSON.stringify(task));
    })
    .catch(function(e) {
      next(e);
    })
});

router.post('/test', function(req, res, next) {
  return res.send(JSON.stringify({
    "message": "tefeest",
    "wefew": req.body.hehe
  }));
});

router.get('/test', function(req, res, next) {
  return res.send(JSON.stringify({
    "message": "test"
  }));
});

// 获取该用户的所有任务
router.get('/list', check.checkLogin, function(req, res, next) {
  let author = req.session.user._id;
  TaskModel
    .getTasks(author)
    .then(function(result) {
      let task = result[0];
      res.send(JSON.stringify([]));
    })
    .catch(function(e) {
      next(e);
    });
});

// 创建一个新的任务
router.post('/create', check.checkLogin, function(req, res, next) {
  let author = req.session.user.email;
  let paramUser = req.body.paramUser;
  let paramLte = req.body.paramLte;
  let paramRadar = req.body.paramRadar;

  // 拼装一个 任务
  let tempTask = {
    author,
    bundle: req.body.bundle
  };

  TaskModel
    .create(tempTask)
    .then(function(result) {
      let task = result.ops[0];
      return task;
    })
    .then(function(task) {
      cache.rpush(TASK_QUEUE_NAME, JSON.stringify(task));
      return res.send(JSON.stringify(task));
    })
    .catch(function(e) {
      next(e);
    });
});

module.exports = router;
