
import urlparse
import urllib

# A slightly "better" urljoin. Doesn't support multi-valued querystring params at the moment
def urljoin(base, url):
    query = {}
    query.update(urlparse.parse_qsl(urlparse.urlparse(base).query))
    query.update(urlparse.parse_qs(urlparse.urlparse(url).query))
    return '%s?%s' % (urlparse.urljoin(base, url), urllib.urlencode(query))
