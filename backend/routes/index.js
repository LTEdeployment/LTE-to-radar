let pub = function(app) {
  app.use('/', require('./tasks'));
  app.use('/signup', require('./signup'));
  app.use('/signin', require('./signin'));
  app.use('/signout', require('./signout'));
  app.use('/tasks', require('./tasks'));
  // 404 page
  app.use(function(req, res) {
    if (!res.headersSent) {
      res.status(404);
      res.json({
        message: 'NOT FOUND'
      });
    }
  });
};

module.exports = pub;
