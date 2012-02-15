
import simplejson as json
from httplib2 import Http

# A Resource represents a collection, actually
class Resource(object):
    def __init__(self, url, fields = None):
        self.url = url
        self.__fields = fields

    def fields(self):
        if self.__fields != None: return self.__fields

        response, content = Http().request(self.url)
        return json.loads(content)

    def save(self):
        # TODO: put/patch
        pass
