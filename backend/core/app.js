'use strict';
const path = require('path');
const express = require('express');
const session = require('express-session');
const MongoStore = require('connect-mongo')(session);
const bodyParser = require('body-parser');
const config = require('config-lite');
const routes = require('../routes');
const winston = require('winston');
const expressWinston = require('express-winston');

const app = express();

app.use(bodyParser.json());
// 设置静态文件目录
app.use(express.static(path.join(__dirname, 'public')));
// session 中间件
app.use(session({
  // 设置 cookie 中保存 session id 的字段名称
  name: config.session.name,
  // 通过设置 secret 来计算 hash 值并放在 cookie 中，使产生的 signedCookie 防篡改
  secret: config.session.secret,
  // don't create session until something stored
  saveUninitialized: false,
  // don't save session if unmodified
  resave: false,
  cookie: {
    // 过期时间，过期后 cookie 中的 session id 自动删除
    maxAge: config.session.maxAge
  },
  // 将 session 存储到 mongodb
  store: new MongoStore({
    // mongodb 地址
    url: config.mongodb
  })
}));

// 处理表单及文件上传的中间件
app.use(require('express-formidable')({
  uploadDir: path.join(__dirname, 'public/img'), // 上传文件目录
  keepExtensions: true // 保留后缀
}));

// 添加模板必需的三个变量
app.use(function(req, res, next) {
  res.locals.user = req.session.user;
  next();
});

// 正常请求的日志
app.use(expressWinston.logger({
  transports: [
    new(winston.transports.Console)({
      json: true,
      colorize: true
    }),
    new winston.transports.File({
      filename: 'logs/success.log'
    })
  ]
}));

// 路由
routes(app);

// 错误请求的日志
app.use(expressWinston.errorLogger({
  transports: [
    new winston.transports.Console({
      json: true,
      colorize: true
    }),
    new winston.transports.File({
      filename: 'logs/error.log'
    })
  ]
}));

// error page
app.use(function(err, req, res, next) {
  res.send(JSON.stringify({
    "fefe": "fefe"
  }));
});

module.exports = app;
