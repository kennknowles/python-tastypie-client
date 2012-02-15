
import simplejson as json
import urllib
from httplib2 import Http

from tastypie_client import Collection
from tastypie_client.url import urljoin

# An API is just a baseUrl from which all schema business is fetched
class Api(object):
    def __init__(self, url):
        self.url = url

    @property
    def schema(self):
        response, content = Http().request(self.url)
        return json.loads(content)

    @property
    def collections(self):
        for name in self.schema.keys():
            yield getattr(self, name)

    def __getattr__(self, attr):
        s = self.schema
        return Collection(url = urljoin(self.url, s[attr]['list_endpoint']),
                          schema_url = urljoin(self.url, s[attr]['schema']))
