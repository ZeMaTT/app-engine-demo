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


class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # inject headers here (self.request.headers)
        super(BaseHandler, self).dispatch()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class TodoHandler(webapp2.RequestHandler):
    payload = [{
        'id': 1,
        'content': 'todo laundry'
    }, {
        'id': 2,
        'content': 'todo lunch'
    }, {
        'id': 3,
        'content': 'todo taxes'
    }]

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.set_status(200)
        self.response.write(json.dumps(self.payload))

    def post(self):
        payload = self.request.body
        data = json.loads(payload)
        logger.debug(data)
        self.payload.append(data)
        self.response.set_status(201)
        self.response.write(json.dumps(data))


APPLICATION_HANDLERS = [
    (r'/api/', MainHandler),
    (r'/api/todos/', TodoHandler),
]

app = webapp2.WSGIApplication(APPLICATION_HANDLERS, debug=True)
