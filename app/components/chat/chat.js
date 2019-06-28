app.controller('friend-list', function ($scope, $http) {
    $http.get('/handlers/chat').then(function(response){
        $scope.contacts = response.data; 
        })
        function getDatafromdb() {
            return $http.get('http://localhost:8080/handlers/get')
            }
});
