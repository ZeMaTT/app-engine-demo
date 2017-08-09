/**
 * Created by matthias on 25/05/2015.
 */
(function (angular) {
    'use strict';

    var apiUrl = "/api", api = {url: apiUrl};
    var Environment = {
        debug: true
    };

    api.todos = {url: apiUrl + "todos/"};
    api.todos.create = api.todos.url;
    api.todos.get = api.todos.url;
    api.todos.list = api.todos.url;
    api.todos.update = api.todos.get;
    api.todos.delete = api.todos.get;
    api.todos.list = api.todos.url;


    angular
        .module('app')
        .constant('Api', api)
        .constant('Environment', Environment);

})(angular);
