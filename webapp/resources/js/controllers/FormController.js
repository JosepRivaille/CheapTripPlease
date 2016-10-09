app.controller('FormController', function($scope, $http) {

    $scope.cities = [{id: ''}];

    $scope.addNewChoice = function () {
        var currentItemNo = $scope.cities.length - 1;
        //if ($scope.cities[currentItemNo]['id'] != "") { //
        //    $scope.cities[currentItemNo]['id'] = 'city_' - currentItemNo;
        //    $scope.cities.push({'id': ''});
        //}
        $scope.cities.push({'id': ''});
    };

    $scope.removeChoice = function() {
        var lastItem = $scope.cities.length - 1;
        if (lastItem >= 1) {
            $scope.cities.splice(lastItem)
        }
    };

    $scope.uploadData = function() {
        var loader = document.querySelector("#loader");
        console.log(loader);
        loader.className = 'display_loader';
        var form_div = document.querySelector(".form-style-9");
        form_div.className = 'hide_form';

        $http({ method: 'POST', url: 'http://127.0.0.1:5000/sendData' })
            .success(function(data, status, headers, config) {
                console.log(data + " " + status);
            }).error(function(data, status, headers, config) {
            console.log("Faaaail " + status);
        });
        $scope.cities = [{id: ''}];
    };

    $scope.receiveData = function () {
        listener();

    };

    var listener = function() {
        var server = app.listen(3000, function () {
            var host = server.address().address;
            var port = server.address().port;
            console.log('Example app listening at http://%s:%s', host, port);
        });
    };

    $scope.onEnterClick = function (event) {
        if (event.keyCode == 13) $scope.addNewChoice();
        else if (event.keyCode == 8) {
            $scope.removeChoice();
            event.preventDefault();
        }
    }

});