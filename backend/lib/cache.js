const redis = require("redis");
const config = require('config-lite');

let client = redis.createClient({
  host: config.redisHost,
  port: config.redisPort
});

module.exports = client;
