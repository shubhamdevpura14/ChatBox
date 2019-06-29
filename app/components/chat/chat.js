 app.controller('message',function ($scope, $http){
    $scope.text = null;
    $scope.postdata = function (text) {
        var data = {
            text: text
        };
        sendData(data)
    }
    function sendData(data) {
        var ss = JSON.stringify(data);
        return $http.post('/handlers/submit', ss)
                                }
        function getDatafromdb() {
        return $http.get('/handlers/ListMsgs')
                               }                        
 });
