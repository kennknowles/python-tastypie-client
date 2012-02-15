
import simplejson as json
from httplib2 import Http
from LazyEvaluation import lazy

# An API is just a baseUrl from which all schema business is fetched
class Api(object):
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def schema(self):
        response, content = Http().request(self.baseUrl)
        return json.loads(content)
