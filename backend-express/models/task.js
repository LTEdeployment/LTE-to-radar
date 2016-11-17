'use strict';
const mongodb = require('../core/mongo');
const tool = require('../core/tool');

const MONGODB_COLLECTION = 'task';

function Task(parcel) {
  this.parcel = parcel;
}

Task.prototype.save = function(callback) {
  let task = this;
  task.createTime = new Date();
  mongodb.open(function(err, db) {
    if (err) {
      return callback(err);
    }
    db.collection(MONGODB_COLLECTION, function(err, collection) {
      if (err) {
        mongodb.close();
        return callback(err, null);
      }
      collection.insert(task, {
        safe: true
      }, function(err, result) {
        mongodb.close();
        if (err) {
          return callback(err);
        }
        callback(null, result.ops);
      });
    });
  });
};

module.exports = Task;
