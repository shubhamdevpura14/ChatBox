app.controller('friend-list',function($scope, $http, $interval){
    $http.get('/handlers/Contacts').then(function(response){

        $scope.owner = response.data.current_user;
        cont_list = JSON.parse(response.data.d)
        $scope.list = cont_list;
    })
      $scope.selected = null;
      $scope.user2 = function(x) {
        $scope.selected = x;
        $interval(a,500);
      }

    $scope.text = null;
    function getDatafromdb() {
        var data = {
            receiver: $scope.selected.email
                   };   
 
        var ss = JSON.stringify(data);
        return $http.post('/handlers/get',ss)
            } 
        function a() {
        getDatafromdb().then( function(response) { 
            $scope.chat = response.data;
        })
        }
      
        $scope.postdata = function (text, e) {
            e.preventDefault();
        var data = {
            text: text,
            receiver: $scope.selected.email
                   };   
 
        var ss = JSON.stringify(data);
        $http.post('/handlers/save', ss)
            }
  });