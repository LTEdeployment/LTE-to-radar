module.exports = {
  port: 8081,
  session: {
    secret: 'compute_secret',
    key: 'compute_key',
    maxAge: 2592000000
  },
  white_origins: [
    'http://localhost:8080',
    'http://compute.xhinliang.com',
    'http://compute.webdev.com'
  ],
  mongodb: 'mongodb://localhost:27017/compute_backend',
  redisPort: 6379,
  redisHost: '127.0.0.1'
}
