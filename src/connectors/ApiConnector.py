'''
Created on 4 juil. 2012

@author: Antoine Lorence
'''

import json
import httplib
import urllib

class ApiConnector:
    
    def __init__(self, api_base) :

        self.baseUrl = api_base
        self.http = httplib.HTTPConnection(api_base, 80)
    
    def query(self, query, params):
        url = query +"?" + urllib.urlencode(params)
        self.http.request("GET", url)
        response = self.http.getresponse()
        jsonResponse = json.load(response)
        return jsonResponse
        