const Task = require('../lib/mongo').Task;

let pub = {};

pub.create = function(task) {
  return Task.create(task).exec();
};

pub.getTaskById = function(id) {
  return Task
    .findOne({
      _id: id
    })
    .populate({
      path: 'author',
      model: 'User'
    })
    .addCreatedAt()
    .exec();
};

pub.getTasks = function(author) {
  var query = {};
  if (author) {
    query.author = author;
  }
  return Task
    .find(query)
    .populate({
      path: 'author',
      model: 'User'
    })
    .sort({
      _id: -1
    })
    .addCreatedAt()
    .exec();
};

module.exports = pub;
