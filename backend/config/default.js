module.exports = {
  port: 3000,
  session: {
    secret: 'myblog',
    name: 'myblog',
    maxAge: 2592000000
  },
  mongodb: 'mongodb://localhost:27017/compute',
  redisPort: 6379,
  redisHost: '127.0.0.1'
};
