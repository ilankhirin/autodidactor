var BACKEND_URL = "http://localhost:5000";

angular.module("autodidactorApp", []);

angular.module("autodidactorApp").controller("autodidactorCtrl", function ($http) {
    var autodidactorVm = this;

    autodidactorVm.searchInput = "";
    autodidactorVm.graphJson = "Not back yet...";

    autodidactorVm.search = function (inputSubject) {
        url = BACKEND_URL + "/getGraph/" + inputSubject;
        $http.get(url).then(function (res) {
            // data = res.data
            // dataMock:
            var data = {
                "css": {
                    "html": 547,
                    "javascript": 339,
                    "json": 20,
                    "promise": 0
                },
                "html": {
                    "css": 383,
                    "javascript": 291,
                    "json": 13,
                    "promise": 0
                },
                "javascript": {
                    "css": 282,
                    "html": 260,
                    "json": 17,
                    "promise": 1
                },
                "json": {
                    "css": 400,
                    "html": 363,
                    "javascript": 627,
                    "promise": 0
                },
                "promise": {
                    "css": 55,
                    "html": 42,
                    "javascript": 945,
                    "json": 20
                }
            };
            autodidactorVm.graphJson = data;
            initializeGraph(data);
        });
    }

    autodidactorVm.getSubjectAutocomlete = function (inputText) {
        console.log(inputText);
        url = BACKEND_URL + "/getAutocomplete/" + inputText;
        $http.get(url)
            .then(function (res) {
                autodidactorVm.subjectOptions = res.data.options;
            });
    }

    function initializeGraph(graphData) {
        graphOperations.initializeGraph(graphData)
    }
});