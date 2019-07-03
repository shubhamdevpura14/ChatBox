app.controller('friend-list',function($scope, $http, $timeout){
    $http.get('/handlers/Contacts').then(function(response){
      $scope.list = response.data; 
      })
      $scope.selected = null;
      $scope.user2 = function(x) {
        $scope.selected = x;
      }
      $http.get('/').then(function(response)
        {$scope.user = response.data;})
// app.controller('message',function ($scope, $http){
    $scope.text = null;
    function getDatafromdb() {
        return $http.get('/handlers/get')
            } 
    function a() {
        getDatafromdb().then( function(d) {
            $scope.data = d.data;
            $scope.sender = d.sender;
            $scope.receiver = d.receiver;
        })
        }
    
    function sendData(data) {
        debugger
        var ss = JSON.stringify(data);
        return $http.post('/handlers/save', ss).then (function(d) {
            $timeout( function(){
                a()
                    }, 500 );
                  return d
            })
    }
      
        $scope.postdata = function (text, selected) {
        var data = {
            text: text,
            receiver: selected.email
                   };   
            debugger  
        sendData(data)


    }
                               
 });
