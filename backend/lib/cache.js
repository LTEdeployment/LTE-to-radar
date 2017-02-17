const redis = require('redis')
const config = require('xconfigjs')

let options = {
  host: config.redis_host,
  port: config.redis_port
}

if (config.redis_password) {
  options.password = config.redis_password
}

let client = redis.createClient(options)

module.exports = client
