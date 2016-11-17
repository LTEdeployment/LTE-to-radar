'use strict';

const domain = require('domain');
const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const mailOptions = require('../config/mail.json');
const app = express();
const mailer = require('express-mailer');

mailer.extend(app, mailOptions);

// babel 编译
require('babel-core/register');

const router = require('./router');
const tool = require('./tool');
const config = require('../config/main');

// 初始化 Express 的一些中间件和参数
app.use(express.static('public'));
app.set('views', __dirname + '/../views');
app.set('view engine', 'jade');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: false
}));
app.use(cookieParser());

// 未处理异常捕获 middleware
app.use(function(req, res, next) {
  let d = domain.create();
  d.add(req);
  d.add(res);
  d.on('error', function(err) {
    console.error('uncaughtException url=%s, msg=%s', req.url, err.stack || err.message || err);
    if (!res.finished) {
      res.statusCode = 500;
      res.setHeader('content-type', 'application/json; charset=UTF-8');
      res.end('uncaughtException');
    }
  });
  d.run(next);
});

// 跨域支持
app.all('/api/*', (req, res, next) => {
  const origin = req.headers.origin;
  tool.debug(`origin: ${origin}`);
  if (config["whiteOrigins"].indexOf(origin) !== -1) {
    res.header('Access-Control-Allow-Origin', origin);
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    res.header('Access-Control-Allow-Credentials', true);
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS, DELETE');
  }
  next();
});

// api
app.use('/api', router);

// 如果任何路由都没匹配到，则认为 404
// 生成一个异常让后面的 err handler 捕获
app.use(function(req, res, next) {
  tool.l('未匹配路由');
  res.sendFile(path.dirname(require.main.filename) + '../../public/index.html');
});

module.exports = app;
