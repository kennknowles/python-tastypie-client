
import simplejson as json
from httplib2 import Http
from urlparse import urljoin

class Collection(object):
    def __init__(self, url, schema_url = None):
        self.url = url
        self.schema_url = schema_url

    def get_all(self):
        response, content = Http().request(self.url)
        return json.loads(content)['objects']
        
    def get(self, id):
        return None
        
    def put(self, id, value):
        return None

    def post(self, id, value):
        return None

    def patch(self, id, changes):
        return None

    def schema(self):
        if self.schema_url:
            response, content = Http().request(self.schema_url)
            return json.loads(content)
