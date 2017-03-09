
var MongoClient = require('mongodb').MongoClient;

//实现获得用户配置文件的路由
exports.getCI = function (req ,res){
	MongoClient.connect('mongodb://localhost:27017/test',function(err, db){
		var collection = db.collection('testCollection');
		collection.find({"name":"test"}).toArray(function(err, result) {
		    if(err){
		      console.log('Error:'+ err);
		  	}     
		    console.log(result);
		 });
	});
}

