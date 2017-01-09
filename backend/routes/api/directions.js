const router = require('express').Router()
const DirectionModel = require('../../models/directions')
const check = require('../../middlewares/apicheck')
var multer = require('multer')
var upload = multer({
  dest: 'uploads/'
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
    .getDirections(author, 20, page)
    .then(function (result) {
      res.send(JSON.stringify(result))
    })
    .catch(function (e) {
      next(e)
    })
})

router.post('/create', check.checkLogin, upload.single('direction'), function (req, res, next) {
  let author = req.session.user.email
  let file = req.file
  let name = req.body.name

  // 拼装一个 任务
  let direction = {
    author,
    file,
    name
  }

  DirectionModel
    .create(direction)
    .then(function (result) {
      let direction = result.ops[0]
      return direction
    })
    .then(function (direction) {
      return res.send(JSON.stringify(direction))
    })
    .catch(function (e) {
      next(e)
    })
})

module.exports = router
