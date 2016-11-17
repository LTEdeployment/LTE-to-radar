'use strict';

let pub = {};

pub.l = function(msg) {
  console.log('\n\n', msg, '\n\n');
};

pub.debug = function(msg) {
  console.log('\n\n', msg, '\n\n');
};

pub.fail = function(res, err) {
  res.status(err.status).send({
    err: err.status,
    msg: err.msg
  });
};

module.exports = pub;
