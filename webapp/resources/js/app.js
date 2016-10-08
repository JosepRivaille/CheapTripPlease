"use strict";

var app = angular.module("cheapTripPlease", ['ngRoute']);

app.config(function($routeProvider) {
    $routeProvider
        .when("/home", {
            name: "home",
            templateUrl: "templates/home.html",
            controller: 'HomeController'
        })
        .when("/map", {
            name: "map",
            templateUrl : "templates/map.html",
            controller: 'MapController'
        })
        .otherwise("/")
});