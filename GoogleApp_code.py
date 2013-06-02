#!/usr/bin/env python
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

import webapp2
import datetime

from google.appengine.ext import db
from google.appengine.api import users

#We log the web service URL, the size of the message (to determine amplification factor) and a timestamp.
class WSLog(db.Model):
  URL = db.StringProperty(required=True)
  time = db.DateTimeProperty(required=False)
  size = db.IntegerProperty(required=False)

class MainHandler(webapp2.RequestHandler):
  def get(self):
    ws = self.request.get('webservice')   
    show = self.request.get('show')
    remove = self.request.get('remove')
    self.response.headers['Content-Type'] = 'text/plain'   
    #PROBABLY REDUNDANT: ONLY POST REQUESTS WILL BE MADE 
    #(If a webservice request is logged (webservice="..."), we append it to the datalog)
    if(len(ws) > 0):
      self.response.write('Triggered from: ' + ws)
      now = datetime.datetime.now()
      l = WSLog(URL=ws, time=now, size=len(self.request.body))
      l.put()
    #Display all entries 
    if(show == 'true'):
      logs = db.GqlQuery("SELECT * FROM WSLog")
      for l in logs:
        self.response.write('URL: ' + l.URL + '\nSIZE: ' + str(l.size) + '\nTIME: ' + l.time.strftime("%Y-%m-%d %H:%M:%S")  + '\n\n')
    #Remove all entries (password 'xxx' is censored here, to prevent abuse)
    if(remove == 'xxx'):
      logs = db.GqlQuery("SELECT * FROM WSLog")
      db.delete(logs)
      self.response.write('Logs removed.')
      
  #If a webservice request is logged (webservice="..."), we append it to the datalog   
  def post(self):
    ws = self.request.get('webservice')
    now = datetime.datetime.now()
    l = WSLog(URL=ws, time=now, size=len(self.request.body))
    l.put()
    
      
app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)



