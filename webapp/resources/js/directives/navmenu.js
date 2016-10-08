app.directive('navmenu', function($route, $rootScope, $location) {
  return {
    restrict: 'E',
    templateUrl: 'templates/navmenu.html',
    link: function (scope, element, attr) {
      scope.currentRoute = '';
      $rootScope.$on('$routeChangeSuccess', function(next, current) {
        scope.currentRoute = $route.current.name;
        console.log($route.current.name);
      });
    }
  };
});