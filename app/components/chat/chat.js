app.controller('friend-list', function ($scope, $http) {
    $http.get('/handlers/chat').then(function(response){
        $scope.contacts = response.data; 
        })
});