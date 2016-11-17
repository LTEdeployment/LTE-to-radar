'use strict';
/**
 * 这个文件中保存了所有的路由信息，而这些路由指向的是 controller 中的方法
 */
const router = require('express').Router();
const taskController = require('../controllers/task');

router.post('task/create', taskController.create);

module.exports = router;
