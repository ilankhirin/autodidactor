var BACKEND_URL = "http://fake";


angular.module("autodidactorApp", []);

angular.module("autodidactorApp").controller("autodidactorCtrl", function($http) {
    var autodidactorVm = this;

    autodidactorVm.searchInput = "Enter subject...";

    autodidactorVm.search = function(inputSubject) {
        url = BACKEND_URL + "/getGraph";
        $http.get(url, {
            params: {
                subject: inputSubject
            }
        }).then(function(data) {
            console.log(data);
        });
    }

    function initializeGraph(graphData) {
        // Initialize the graph
    }
});