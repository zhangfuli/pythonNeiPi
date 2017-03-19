var MongoClient = require('mongodb').MongoClient;

global.CI = {};
//实现获得用户配置文件的路由
exports.getCI = function (req ,res){
	MongoClient.connect('mongodb://localhost:27017/test',function(err, db){
		var collection = db.collection('testCollection');
		collection.find({"name":"test"}).toArray(function(err, result, req, res) {
		    if(err){
		      	console.log('Error:'+ err);
		  	}else{
		  		global.CI = result;
		  		console.log(global.CI)
		  	}     
		 });
	});
	setTimeout(function (){
		res.json(global.CI);
	},300);
}

