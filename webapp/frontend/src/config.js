/**
 * Created by matthias on 25/05/2015.
 */

(function (angular) {
    "use strict";

    angular
        .module('app')
        .config(configure)
    ;

    configure.$inject = ['$logProvider', 'Environment'];

    function configure($logProvider, Environment) {
        $logProvider.debugEnabled(Environment.debug);
    }

})(angular);
