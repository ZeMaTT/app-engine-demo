/**
 * Created by matthias on 17/07/17.
 */

(function (angular) {
    "use strict";

    angular
        .module('app')
        .controller('MainController', MainController);

    MainController.$inject = ['$log'];

    function MainController(log) {
        var vm = this;

        vm.name = "D2SI";

        activate();

        ////////////////////////

        function activate() {
            log.debug('MainController');
            vm.todos = [
                {title: "todo1", content: "content1"},
                {title: "todo2", content: "content2"},
                {title: "todo3", content: "content3"},
                {title: "todo4", content: "content4"}
            ];
        }
    }

})(angular);