/**
 * Created by matthias on 25/05/2015.
 */
(function (angular) {
    'use strict';

    var Environment = {
        debug: true
    };

    angular
        .module('app')
        .constant('Environment', Environment);

})(angular);
