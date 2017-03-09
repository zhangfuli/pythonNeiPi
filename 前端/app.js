var express = require('express');
module.exports = function (app) {
	var users = require('./controllers/users_controller');
	app.use('/static' , express.static('./static'));
	app.get('/',function (req,res){
		if(req.session.user){
			res.render('index',{ username : req.session.username ,
								 msg : req.session.msg});
		}else{
			req.session.msg = 'Access denied!';
			res.redirect('/login');
		}
	});
	app.get('/user' ,users.getCI);
};
