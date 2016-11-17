'use strict';
const path = require('path');
const express = require('express');
const session = require('express-session');
const MongoStore = require('connect-mongo')(session);
const bodyParser = require('body-parser');
const config = require('config-lite');
const routes = require('./routes');
const winston = require('winston');
const expressWinston = require('express-winston');

const app = express();

app.use(bodyParser.json());
// 设置静态文件目录
app.use(express.static(path.join(__dirname, 'public')));
// session 中间件
app.use(session({
  name: config.session.name, // 设置 cookie 中保存 session id 的字段名称
  secret: config.session.secret, // 通过设置 secret 来计算 hash 值并放在 cookie 中，使产生的 signedCookie 防篡改
  saveUninitialized: false, // don't create session until something stored
  resave: false, // don't save session if unmodified
  cookie: {
    maxAge: config.session.maxAge // 过期时间，过期后 cookie 中的 session id 自动删除
  },
  store: new MongoStore({ // 将 session 存储到 mongodb
    url: config.mongodb // mongodb 地址
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
  res.send(JSON.stringify(err));
});

module.exports = app;
