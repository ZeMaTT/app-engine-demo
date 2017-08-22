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

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

TODOS_LIST = [{
    'id': 1,
    'content': 'todo laundry'
}, {
    'id': 2,
    'content': 'todo lunch'
}, {
    'id': 3,
    'content': 'todo taxes'
}]


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class TodoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.set_status(200)
        self.response.write(json.dumps(TODOS_LIST))

    def post(self):
        payload = self.request.body
        data = json.loads(payload)
        logger.debug(data)
        TODOS_LIST.append(data)
        self.response.set_status(201)
        self.response.write(json.dumps(data))


class TodoDetailsHandler(webapp2.RequestHandler):
    def delete(self, todo_id):
        self.response.set_status(200)
        self.response.write('Not Implemented Yet')

    def get(self, todo_id):
        r = None
        todo_id = int(todo_id)
        print type(todo_id), TODOS_LIST
        for todo in TODOS_LIST:
            if todo['id'] == todo_id:
                r = todo
        if r is None:
            self.response.set_status(404)
            self.response.write(json.dumps({'msg': 'Todo not found'}))
        else:
            self.response.set_status(200)
            self.response.write(json.dumps(r))

    def patch(self, todo_id):
        self.response.set_status(200)
        self.response.write('Not Implemented Yet')

    def put(self, todo_id):
        self.response.set_status(200)
        self.response.write('Not Implemented Yet')


APPLICATION_HANDLERS = [
    (r'/api/', MainHandler),
    (r'/api/todos/', TodoHandler),
    webapp2.Route(r'/api/todos/<todo_id:\d+>/', handler=TodoDetailsHandler, name='todo_id'),
]

app = webapp2.WSGIApplication(APPLICATION_HANDLERS, debug=True)
