var app = angular.module("myApp", ["ngRoute"]);

var api = 'http://127.0.0.1:8000/productID/?format=api';

app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "pages/home-en-2.html"
        }).when("/aboutUs-en", {
            templateUrl: "pages/aboutUs-en.html",
        }).when("/wholeSales-en", {
            templateUrl: "pages/wholeSales-en.html.html"
        }).when("/retailSales-en", {
            templateUrl: "pages/catalog-retail-en.html"
        }).when("/catalog-en", {
            templateUrl: "pages/catalog-retail-en.html"
        }).when("/information-en", {
            templateUrl: "pages/information-en.html"
        }).when("/news-en", {
            templateUrl: "pages/news-en.html"
        }).when("/contactUs-en", {
            templateUrl: "pages/contactUs-en.html"
        }).when("/signIn-en", {
            templateUrl: "pages/signIn-en.html"
        }).when("/signUp-en", {
            templateUrl: "pages/signUp-en.html"
        }).when("/signUp-retail-en", {
            templateUrl: "pages/signUp-retail-en.html"
        }).when("/signUp-whole-en", {
            templateUrl: "pages/signUp-whole-en.html"
        });
}]);


app.controller('mainController', function ($scope,$http) {

    $scope.showNano = false;
    $scope.showPeluche = false;
    $scope.showLoyal = false;

    $scope.payment = true;
    $scope.sizeTable = false;
    $scope.discount = false;

    $scope.faq = false;

    $scope.hats = false;
    $scope.linen = false;
    $scope.socks = false;
    $scope.formal = false;
    $scope.sportswear = false;
    $scope.accessories = false;
    $scope.outwear = false;
    $scope.kids = false;
    $scope.newborn = false;


    $scope.quickHide = function () {
        $scope.hats = false;
        $scope.linen = false;
        $scope.socks = false;
        $scope.formal = false;
        $scope.sportswear = false;
        $scope.accessories = false;
        $scope.outwear = false;
        $scope.kids = false;
        $scope.newborn = false;
    }

    $scope.hatsF = function () {
        $scope.quickHide();
        $scope.hats = !$scope.hats;
    }
    $scope.linenF = function () {
        $scope.quickHide();
        $scope.linen = true;
    }
    $scope.socksF = function () {
        $scope.quickHide();
        $scope.socks = true;
    }
    $scope.formalF = function () {
        $scope.quickHide();
        $scope.formal = true;
    }
    $scope.sportswearF = function () {
        $scope.quickHide();
        $scope.sportswear = true;
    }
    $scope.accessoriesF = function () {
        $scope.quickHide();
        $scope.accessories = true;
    }
    $scope.outwearF = function () {
        $scope.quickHide();
        $scope.outwear = true;
    }
    $scope.kidsF = function () {
        $scope.quickHide();
        $scope.kids = true;
    }
    $scope.newbornF = function () {
        $scope.quickHide();
        $scope.newborn = true;
    }

    $scope.allFalseF = function () {
        $scope.payment = false;
        $scope.sizeTable = false;
        $scope.discount = false;

        $scope.faq = false;
    }

    $scope.faqF = function () {

        $scope.allFalseF();
        $scope.faq = true;
    }

    $scope.paymentF = function () {

        $scope.allFalseF();
        $scope.payment = true;
    }

    $scope.sizeTableF = function () {
        $scope.allFalseF();
        $scope.sizeTable = true;

    }

    $scope.discountF = function () {
        $scope.allFalseF();
        $scope.discount = true;

    }


    
    $scope.one_piece = function(){
        $http.get(api).then(function(response){
            allProducts = response.data;
        })
    };
});


//var initMap = function() {
//    var map = new google.maps.Map(document.getElementById('map'), {
//        center: { lat: 50.5, lng: 30.5 },
//        scrollwheel: false,
//        zoom: 15
//    });
//}
