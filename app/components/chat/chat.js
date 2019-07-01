app.controller('friend-list',function($scope,$http){
    $http.get('/handlers/ListMsgs').then(function(response){
      $scope.list = response.data; 
      })
      $scope.selected = null;
      $scope.user2 = function(x) {
        $scope.selected = x;
      }
  });
/* app.controller('message',function ($scope, $http){
    $scope.text = null;
    $scope.postdata = function (text) {
        var data = {
            text: text
 
        };
        sendData(data)
        getDatafromdb(qry)

    }
    function sendData(data) {
        var ss = JSON.stringify(data);
        return $http.post('/handlers/save', ss)
                                }
        function getDatafromdb() {
        return $http.get('/handlers/')
                               }                        
 });
*/