
import simplejson as json
from httplib2 import Http

from tastypie_client import Resource
from tastypie_client.url import urljoin

class Collection(object):
    def __init__(self, url, schema_url = None):
        self.url = url
        self.schema_url = schema_url

    def get_all(self):
        response, content = Http().request(self.url)
        for obj in json.loads(content)['objects']:
            yield Resource(url = urljoin(self.url, obj['resource_uri']), fields = obj)
        
    def get(self, id):
        return Resource(urljoin(self.url, id))
        
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
