app.controller('FormController', function($scope) {

    $scope.cities = [{id: 'city1'}, {id: 'city2'}];

    $scope.addNewChoice = function () {
        console.log("dd");
        var newItemNo = $scope.cities.length + 1;

        $scope.cities.push({'id': 'choice' + newItemNo});
    };

    $scope.removeChoice = function () {
        var lastItem = $scope.cities.length - 1;
        $scope.cities.splice(lastItem);
    };

});