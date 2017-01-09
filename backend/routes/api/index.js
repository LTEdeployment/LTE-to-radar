var express = require('express')
var router = express.Router()

router.get('/', function (req, res) {
  res.redirect('/user/profile')
})
router.use('/user', require('./user'))
router.use('/tasks', require('./tasks'))
router.use('/directions', require('./directions'))

module.exports = router
