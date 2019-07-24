

app.controller('friend-list',function($scope, $http, $timeout){
    $http.get('/handlers/Contacts').then(function(response){
        debugger
        $scope.owner = response.data.current_user;
        cont_list = JSON.parse(response.data.d)
        $scope.list = cont_list;
    })
      $scope.selected = null;
      $scope.user2 = function(x) {
        $scope.selected = x;
      }

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
      
        $scope.postdata = function (text, e) {
            e.preventDefault();
        var data = {
            text: text,
            receiver: $scope.selected.email
                   };   
 
                   var ss = JSON.stringify(data);
                   return $http.post('/handlers/save', ss).then (function(d) {
                       $timeout( function(){
                           a()
                               }, 500 );
                             return d
                       })

    }
  });