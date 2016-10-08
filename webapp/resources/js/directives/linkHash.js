app.directive('linkHash', function($route, $rootScope, $location) {
    return {
        restrict: 'A',
        link: function (scope, element, attr) {
            element[0].addEventListener("click", function(){
                $location.hash("#/"+attr.linkHash);
            });
            $rootScope.$on('$routeChangeSuccess', function(next, current) {
                var elements = document.querySelectorAll("[link-hash]");
                for (var i = 0; i < elements.length; i++) {
                    elements[i].classList.remove("active");
                }
                elements = document.querySelectorAll("[link-hash="+$route.current.name+"]");
                for (i = 0; i < elements.length; i++) {
                    elements[i].classList.add("active");
                }

            });
        }
    };
});