var app = angular.module("simpleApp",['ngMaterial', 'ngMessages']);
app.controller("simpleController", function ($scope){
 
$scope.col=[];
 $scope.add= function()
{
   $scope.col.push($scope.data);
   $scope.data="";
}
})


