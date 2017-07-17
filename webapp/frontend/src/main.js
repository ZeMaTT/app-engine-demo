/**
 * Created by matthias on 17/07/17.
 */

(function (angular) {
    "use strict";
    angular.module('app')
        .controller('MainController', MainController);

    MainController.$inject = ['$log'];

    function MainController(log) {
        var vm = this;


        activate();

        ////////////////////////

        function activate() {
            log.debug('MainController');
        }
    }

})(angular);