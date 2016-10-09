app.controller('FormController', function($scope, $http) {

    $scope.cities = [{id: ''}];

    $scope.addNewChoice = function() {
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

        var indata = {
            'originCity': '2',
            'startDate': '3',
            'destinationCity': '4',
            'endDate': '5',
            'citiesList': '6'
        };

        $http({
            method: 'POST',
            url: 'http://127.0.0.1:5000/sendData',
            params: indata
        }).success(function(data, status, headers, config) {
            console.log(data + " " + status);
        }).error(function(data, status, headers, config) {
            console.log("FAIL " + status);
        });
        $scope.cities = [{id: ''}];
    };

    $scope.downloadData = function() {
        var loader = document.querySelector("#loader");
        console.log(loader);
        loader.className = '';

        $http({
            method: 'GET',
            url: 'http://127.0.0.1:5000/getData'
        }).success(function (response, status, headers, config) {
            response.forEach(function(cityObject) {
                console.log(cityObject.name)
            });
        }).error(function (data, status, headers, config) {
            console.log("FAIL " + status);
        })
    }

    $scope.autocompleteData = function(event) {
        $http({ method: 'POST', url: 'http://127.0.0.1:5000/autocomplete/' + '123'})
            .success(function(data, status, headers, config) {
                var placesList = $scope.existingCities = data['Places'];
                var autocompleteData = [];
                placesList.forEach(function(object) {
                    autocompleteData.append(object['PlaceName']);
                });
            }).error(function(data, status, headers, config) {
            console.log("FAIL " + status);
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