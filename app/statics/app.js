'use strict';

// Declare app level module which depends on views, and core components
var app = angular.module('myApp', [
  'ngRoute',
  'ngMaterial', 'ngAnimate', 'ngAria'
])

// .controller('AppCtrl', function ($scope, $mdSidenav) {
//     $scope.toggleLeft = buildToggler('left');

//     function buildToggler(componentId) {
//       return function() {
//         $mdSidenav(componentId).toggle();
//       };
//     }
//   });
app.
config(function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');

  $routeProvider
  .when("/", {
    template : ""
  })
  /*.when("/login", {
    templateUrl : "/component/login/login.html"
  })*/
  .when("/chat", {
    templateUrl : "component/chat/chat.html",
    controller: 'friend-list'
    })
  //.otherwise({redirectTo: '/login'});
});

