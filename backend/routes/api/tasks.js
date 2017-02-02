const router = require('express').Router()
const TaskModel = require('../../models/tasks')
const check = require('../../middlewares/apicheck')
const cache = require('../../lib/cache')
const config = require('config-lite')

// 根据任务 ID 查询指定的任务
// TODO 不能找到相应的任务，原因估计在 Mongolass 上
router.get('/id/:id', check.checkLogin, function (req, res, next) {
  let id = req.params.id
  TaskModel
    .getTaskById(id)
    .then(function (result) {
      res.send(JSON.stringify(result))
    })
    .catch(function (e) {
      next(e)
    })
})

// 获取该用户的任务列表
router.get('/list/:page', check.checkLogin, function (req, res, next) {
  let author = req.session.user.email
  let page = req.params.page
  TaskModel
    .getTasks(author, 20, page)
    .then(function (result) {
      res.send(JSON.stringify(result))
    })
    .catch(function (e) {
      next(e)
    })
})

// 创建一个新的任务
router.post('/create', check.checkLogin, function (req, res, next) {
  let author = req.session.user.email
  let bundle = req.body.bundle
  let name = req.body.name
  let description = req.body.description

  // 拼装一个 任务
  let tempTask = {
    author,
    bundle,
    name,
    description
  }

  TaskModel
    .create(tempTask)
    .then(function (result) {
      let task = result.ops[0]
      return task
    })
    .then(function (task) {
      cache.rpush(config.redis_task_lte_queue, JSON.stringify(task))
      return res.json({
        code: 0,
        message: 'ok',
        data: task
      })
    })
    .catch(function (e) {
      if (e.message.match('E11000 duplicate key')) {
        return res.json({
          code: -1,
          message: '这个名字的计算任务已经存在了哈!'
        })
      }
      next(e)
    })
})

module.exports = router
