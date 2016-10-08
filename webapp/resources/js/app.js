"use strict";

var app = angular.module("cheapTripPlease", ['ngRoute']);

app.config(function($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl : "templates/home.html",
            controller: 'MainController'
        })
        .when("/map", {
            templateUrl : "templates/map.html",
            controller: 'MainController'
        })
});