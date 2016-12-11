module.exports = {
  port: 8081,
  session: {
    secret: 'ewfwete',
    key: 'tefewfew',
    maxAge: 2592000000
  },
  white_origins: [
    "http://localhost:8080",
    "http://compute.xhinliang.com"
  ],
  mongodb: 'mongodb://localhost:27017/comp-ewf',
  redisPort: 6379,
  redisHost: '127.0.0.1'
};
