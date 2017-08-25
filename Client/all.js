var BACKEND_URL = "http://localhost:5000";

angular.module("autodidactorApp", ["autocomplete"]);

angular.module("autodidactorApp").controller("autodidactorCtrl", function ($http, $timeout) {
    var vm = this;

    vm.searchText = "";
    vm.graphJson = "Not back yet...";

    vm.search = function (inputSubject) {
        url = BACKEND_URL + "/getGraph/" + inputSubject;
        $http.get(url).then(function (res) {
            data = res.data
            vm.graphJson = data;
            initializeGraph(data);
        });
    }

    vm.getSubjectAutocomlete = _.throttle(getSubjectAutocomlete, 1000);

    function getSubjectAutocomlete(inputText) {
        url = BACKEND_URL + "/getAutocomplete/" + inputText;
        $http.get(url)
            .then(function (res) {
                $timeout(function () {
                    vm.subjectOptions = res.data.options;
                }, 0);
            });
    }

    function initializeGraph(graphData) {
        graphOperations.initializeGraph(graphData)
    }
});