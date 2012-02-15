
import sys

from tastypie_client import Api

# A crawl is (for now) a sequence of URLs discovered and the status code that resulted in
# pulling it down. New URLs are discovered by traversing the JSON that comes back from
# the server. This is very *very* naive and not.
class Crawl(object):
    def __init__(self, api):
        self.api = api


    def urls(self):
        visited = set()
        def visit(url):
            if url in visited:
                return False
            else:
                visited.add(url)
                return True
            
        visit(self.api.url)
        print self.api.url

        for collection in self.api.collections:
            if visit(collection.url): 
                yield collection.url
            else:
                continue

            for resource in collection.get_all():
                if visit(resource.url):
                    yield resource.url
                else:
                    continue

if __name__ == '__main__':
    url = sys.argv[1]
    for discovered_url in Crawl(Api(url)).urls():
        print discovered_url
