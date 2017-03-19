angular.module('myApp' , ['ngRoute','chart.js']).
	controller('myController' ,['$scope','$http',function ($scope ,$http) {
		$scope.Y = [];
	    $scope.X = [];
		$http.get('/user/getCI').success(function (data ,status ,headers ,config){
			$scope.user = data;
			console.log(data);
			for(var i = 0; i<data.length; i ++) {
				$scope.X.push(data[i].time);
	        	$scope.Y.push(data[i].CI);
	      	}
		});
	    $scope.labels = $scope.X;
	    $scope.data = $scope.Y;
	    $scope.onClick = function (points, evt) {
	      console.log(points, evt);
	    };
	    $scope.datasetOverride = [{ yAxisID: 'y-axis-1'}];
	    $scope.options = {
	      scales: {
	        yAxes: [
	          {
	            id: 'y-axis-1',
	            type: 'linear',
	            display: true,
	            position: 'left'
	          }
	        ]
	      }
	    };
	}]);