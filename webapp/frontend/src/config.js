/**
 * Created by matthias on 25/05/2015.
 */

(function (angular) {
    "use strict";

    angular
        .module('app')
        .config(configure)
    ;

    configure.$inject = ['$logProvider'];

    function configure($logProvider) {
        $logProvider.debugEnabled(true);
    }

})(angular);
