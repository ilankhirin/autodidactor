var BACKEND_URL = "http://localhost:5000";
var SUBJECT_AUTOCOMPLETE_URL = "https://en.wikipedia.org/w/api.php";
var SUBJECT_AUTOCOMPLETE_PARAMS = {
    action: "opensearch",
    format: "json",
    formatversion: 2,
    search: "",
    namespace: 0,
    limit: 10,
    suggest: true
};

angular.module("autodidactorApp", []);

angular.module("autodidactorApp").controller("autodidactorCtrl", function($http) {
    var autodidactorVm = this;

    autodidactorVm.searchInput = "Enter subject...";
    autodidactorVm.graphJson = "Not back yet...";

    autodidactorVm.search = function(inputSubject) {
        url = BACKEND_URL + "/getGraph/" + inputSubject;
        $http.get(url).then(function(data) {
            console.log(data);
            autodidactorVm.graphJson = data;
        });
    }

    autodidactorVm.getSubjectAutocomlete = function(inputText) {
        console.log(inputText);
        debugger;
        url = BACKEND_URL + "/getAutocomplete/" + inputText;

        SUBJECT_AUTOCOMPLETE_PARAMS.search = inputText;
        $http.get(url)
            .then(function(res) {
                debugger;
            },
            function(res) {
                debugger;
            });
    }

    function initializeGraph(graphData) {
        // Initialize the graph
    }
});