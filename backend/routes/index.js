module.exports = function (app) {
  app.get('/', function (req, res) {
    res.redirect('/user/profile')
  })
  app.use('/user', require('./user'))
  app.use('/api', require('./api'))

  // 404 page
  app.use(function (req, res) {
    if (!res.headersSent) {
      res.render('404')
    }
  })
  // error page
  app.use(function (err, req, res, next) {
    res.render('error', {
      error: err
    })
  })
}
