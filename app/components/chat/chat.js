app.controller('friend-list',function($scope, $http, $timeout){
    $http.get('/handlers/ListMsgs').then(function(response){
      $scope.list = response.data; 
      })
      $scope.selected = null;
      $scope.user2 = function(x) {
        $scope.selected = x;
      }

// app.controller('message',function ($scope, $http){
    $scope.text = null;
    function getDatafromdb() {
        return $http.get('/handlers/get')
            } 
    function a() {
        getDatafromdb().then( function(d) {
            $scope.data = d.data;

        })
        }
    
    function sendData(data) {
        var ss = JSON.stringify(data);
        return $http.post('/handlers/save', ss).then( function(d) {
            $timeout( function(){
                a()
                    }, 5000 );
                  return d
            })
    }
      
        $scope.postdata = function (text) {
        var data = {
            text: text,
                   };
        sendData(data)


    }
                               
 });
