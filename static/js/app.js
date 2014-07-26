
//configuramos angular para que trabaje con [[]]
angular.module('myapp', []).
    config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    });


//controlador
function indiciosCtrl($scope) {
    $scope.lista = [];

    //agregar
    $scope.add = function () {
        if ($scope.indicio != null) {
            $scope.lista.push({
                nombre: $scope.indicio
            });
            $scope.indicio = null;
            //metodo de jquery
            $("#indicio").focus();
        } else {
            alert("ingrese un indicio valido");
            return false;
            $("#indicio").focus();
        }
    }

    //eliminar
    $scope.remove = function (id) {
        $scope.lista.splice(id, 1);
    }

}