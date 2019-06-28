'use strict';

// Declare app level module which depends on views, and core components
var app = angular.module('myApp', [
  'ngRoute',
  'ngMaterial', 'ngAnimate', 'ngAria'
])
app.
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');

  $routeProvider
  .when("/", {
    template : "go to login page <a href='/#!/login'>login</a>"
  })
  .when("/login", {
    templateUrl : "/component/login/login.html"
  })
  .when("/chat", {
    templateUrl : "/component/chat/chat.html"
  })
  .otherwise({redirectTo: '/login'});
}]);

