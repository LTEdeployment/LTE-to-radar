let pub = function(app) {
    app.use('/', require('./signup'));
    app.use('/signup', require('./signup'));
    app.use('/signin', require('./signin'));
    app.use('/signout', require('./signout'));
    app.use('/tasks', require('./tasks'));
    // 404 page
    app.use(function(req, res) {
        if (!res.headersSent) {
            res.render('404');
        }
    });
};

module.exports = pub;
