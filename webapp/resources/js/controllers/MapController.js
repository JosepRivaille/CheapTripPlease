app.controller('MapController', ['$scope', function ($scope, $route) {

    $scope.markers = [];

    $scope.addNewMarker = function(lat, lng) {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(100, -5),
            map: map,
            title: 'Hello World!'
        });
    };

    $scope.createMap = function() {
        var mapCanvas = document.getElementById("map");
        var mapOptions = {
            center: new google.maps.LatLng(51.5, -0.2),
            disableDefaultUI: true,
            draggable: false,
            zoom: 3,
            mapTypeId: 'satellite'
        };
        var map = new google.maps.Map(mapCanvas, mapOptions);
    }
}]);