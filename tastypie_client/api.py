
import simplejson as json
from httplib2 import Http
from urlparse import urljoin
from LazyEvaluation import lazy

from tastypie_client import Collection

# An API is just a baseUrl from which all schema business is fetched
class Api(object):
    def __init__(self, url):
        self.url = url

    @property
    def schema(self):
        response, content = Http().request(self.url)
        return json.loads(content)

    def __getattr__(self, attr):
        s = self.schema
        return Collection(urljoin(self.url, s[attr]['list_endpoint']), 
                          urljoin(self.url, s[attr]['schema']))
