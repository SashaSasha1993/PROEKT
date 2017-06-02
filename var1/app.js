var app = angular.module("myApp", ["ngRoute"]);

app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
    //$locationProvider.html5Mode(true);
    $routeProvider.when("/", {
        templateUrl: "templates/home-en-t.html"
    }).when("/catalog-retail", {
        templateUrl: "templates/catalog-retail-en.html",
    }).when("/aboutUs", {
        templateUrl: "templates/aboutUs-en.html.html"
    }).when("/contact", {
        templateUrl: "templates/contact.html"
    });
}]);