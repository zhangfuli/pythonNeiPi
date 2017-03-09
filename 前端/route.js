var express = require('express');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var conn = mongoose.connect('mongodb://localhost:27017/test');
var app = express();

app.engine('.html',require('ejs').__express);
app.set('views', __dirname + '/views');
app.set('view engine','html');
app.use(bodyParser());
app.use(cookieParser());


require('./app')(app);
app.listen(80);
