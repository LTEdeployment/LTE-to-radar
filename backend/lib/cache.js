const redis = require('redis')
const config = require('config-lite')

let client = redis.createClient({
  host: config.redis_host,
  port: config.redis_port
})

module.exports = client
