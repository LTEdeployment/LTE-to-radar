const Direction = require('../lib/mongo').Direction
let pub = {}

pub.create = function (direction) {
  return Direction
    .create(direction)
    .exec()
}

pub.getDirectionById = function (id) {
  return Direction
    .findOne({
      _id: id
    })
    .populate({
      path: 'author',
      model: 'User'
    })
    .addCreatedAt()
    .exec()
}

pub.getDirections = function (author, limit, page) {
  var query = {}
  if (author) {
    query.author = author
  }
  return Direction
    .find(query)
    .skip((page - 1) * limit)
    .limit(limit)
    .populate({
      path: 'author',
      model: 'User'
    })
    .sort({
      _id: -1
    })
    .addCreatedAt()
    .exec()
}

module.exports = pub
