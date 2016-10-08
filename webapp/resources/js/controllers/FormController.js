app.controller('FormController', function($scope, $http) {

    $scope.cities = [{id: 'city1'}, {id: 'city2'}];

    $scope.addNewChoice = function () {
        console.log("dd");
        var newItemNo = $scope.cities.length + 1;

        $scope.cities.push({'id': 'choice' + newItemNo});
    };

    $scope.removeChoice = function() {
        var lastItem = $scope.cities.length - 1;
        $scope.cities.splice(lastItem);
    };

    $scope.uploadData = function() {
        $http({ method: 'POST', url: 'http://127.0.0.1:5000/sendData' })
            .success(function(data, status, headers, config) {
                console.log(data + " " + status);
            }).error(function(data, status, headers, config) {
            console.log("Faaaail " + status);
        });
    };

});