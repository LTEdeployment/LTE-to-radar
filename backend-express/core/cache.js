const redis = require("redis");
const dbConfig = require("../config/db.json");
let client = redis.createClient({
  host: dbConfig['redis_host'],
  port: dbConfig['redis_port'],
});

module.exports = client;
