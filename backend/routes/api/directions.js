const router = require('express').Router()
const multer = require('multer')
const uuidV4 = require('uuid/v4')
const DirectionModel = require('../../models/directions')
const check = require('../../middlewares/apicheck')
const cache = require('../../lib/cache')
const config = require('config-lite')

let storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, './uploads/')
  },
  filename: function (req, file, cb) {
    cb(null, uuidV4() + '.mat')
  }
})

let upload = multer({
  storage
})

router.get('/id/:id', check.checkLogin, function (req, res, next) {
  let id = req.params.id

  DirectionModel
    .getDirectionById(id)
    .then(function (result) {
      res.send(JSON.stringify(result))
    })
    .catch(function (e) {
      next(e)
    })
})

// 分页展示方向图，每页20
router.get('/list/:page', check.checkLogin, function (req, res, next) {
  let author = req.session.user.email
  let page = req.params.page

  DirectionModel
    .getDirections(author, 10, page)
    .then(function (result) {
      res.send(JSON.stringify(result))
    })
    .catch(function (e) {
      next(e)
    })
})

router.get('/all', check.checkLogin, function (req, res, next) {
  let author = req.session.user.email

  DirectionModel
    .getAllNames(author)
    .then(function (result) {
      res.json({code: 0, message: 'ok', data: result})
    })
    .catch(function (e) {
      res.json({code: -1, message: 'bu ok', data: null})
    })
})

router.get('/amount', check.checkLogin, function (req, res, next) {
  let author = req.session.user.email

  DirectionModel
    .getAmount(author)
    .then(function (amount) {
      res.json({code: 0, message: 'ok', data: amount})
    })
    .catch(function (e) {
      res.json({code: -1, message: e.message, data: null})
    })
})

router.post('/create', check.checkLogin, upload.single('direction'), function (req, res, next) {
  let author = req.session.user.email
  let file = req.file
  let name = req.body.name
  let description = req.body.description

  // 拼装一个 任务
  let direction = {
    author,
    file,
    name,
    description
  }

  DirectionModel
    .create(direction)
    .then(function (directionSave) {
      cache.rpush(config.redis_mat_directions_queue, JSON.stringify(direction))
      return res.json({code: 0, message: 'ok', data: directionSave})
    })
    .catch(function (e) {
      if (e.message.match('E11000 duplicate key')) {
        return res.json({
          code: -1,
          message: '这个名字的方向图已经存在了哈!'
        })
      }
      return res.json({code: -1, message: e.message, data: null})
    })
})

module.exports = router
