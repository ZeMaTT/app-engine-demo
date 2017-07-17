#!/usr/bin/env python2
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# from google.appengine.api import users
import json
import logging

import webapp2

import models

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # inject headers here (self.request.headers)
        super(BaseHandler, self).dispatch()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class TodoHandler(webapp2.RequestHandler):
    def get(self):
        todos = models.Todo.query().fetch()
        self.response.set_status(200)
        # logger.info('%s %s', todos[0].key, todos[0].key.urlsafe())
        payload = []
        for todo in todos:
            data = todo.to_dict()
            data['id'] = todo.key.urlsafe()
            payload.append(data)
        self.response.write(json.dumps(payload))

    def post(self):
        payload = self.request.body
        data = json.loads(payload)
        logger.debug(data)

        # todo = models.Todo()
        todo = models.Todo(**data)
        todo.put()
        self.response.set_status(201)
        self.response.write(json.dumps(todo.to_dict()))


class TodoDetailsHandler(webapp2.RequestHandler):
    def delete(self, todo_id):
        self.response.set_status(200)
        self.response.write('Not Implemented Yet')

    def get(self, todo_id):
        todo = models.Todo.get(todo_id)
        payload = todo.to_dict()
        payload['id'] = todo.key.urlsafe()
        self.response.set_status(200)
        self.response.write(json.dumps(payload))

    def patch(self, todo_id):
        self.response.set_status(200)
        self.response.write('Not Implemented Yet')

    def put(self, todo_id):
        self.response.set_status(200)
        self.response.write('Not Implemented Yet')


APPLICATION_HANDLERS = [
    (r'/api/', MainHandler),
    (r'/api/todos/', TodoHandler),
    (r'/api/todos/(.*)/', TodoDetailsHandler),
]

app = webapp2.WSGIApplication(APPLICATION_HANDLERS, debug=True)
