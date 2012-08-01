"""

    diffbot -- diffbot API
    ======================

    >>> api = DiffBot('<my api token>')
    >>> api.article('http://google.com', summary=True)
    {...}

"""

import urllib
import urlparse
import simplejson as json
from urllib3 import HTTPConnectionPool

__all__ = ('DiffBot',)

class DiffBot(object):
    """ DiffBot API client

    :param token:
        API token to use
    :keyword pool:
        pool to use for making requests to diffbot API
    :keyword pool_size:
        pool size (only applicable if no ``pool`` argument is passed)
    """

    API_ARTICLE = '/api/article'
    API_FRONTPAGE = '/api/frontpage'

    def __init__(self, token, pool=None, pool_size=1):
        if pool is None:
            pool = HTTPConnectionPool('www.diffbot.com')
        self.pool = pool
        self.token = token

    def _get_request(self, url, params):
        if not 'token' in params:
            params['token'] = self.token
        r = self.pool.request('GET', url, params)
        return json.loads(r.data)

    def _post_request(self, url, params, data):
        if not 'token' in params:
            params['token'] = self.token
        url = add_params(url, params)
        r = self.pool.urlopen(
            'POST', url, body=data,
            headers={'Content-Type': 'text/html'})
        return json.loads(r.data)

    def article(self, url, **params):
        """ Process ``url`` as an article"""
        data = {'url': url}
        data.update(params)
        if 'data' in params:
            return self._post_request(self.API_ARTICLE, data, data.pop('data'))
        else:
            return self._get_request(self.API_ARTICLE, data)

    def frontpage(self, url, **params):
        """ Process ``url`` as a frontpage"""
        data = {'url': url}
        data.update(params)
        if 'data' in params:
            return self._post_request(self.API_FRONTPAGE, data, data.pop('data'))
        else:
            return self._get_request(self.API_FRONTPAGE, data)

def add_params(url, params):
    """ Add params to ``url`` preserving ones already there"""
    parsed = urlparse.urlparse(url)
    parsed_qs = urlparse.parse_qsl(parsed.query)
    parsed_qs = params.items() + parsed_qs
    parsed = parsed._replace(query=urllib.urlencode(parsed_qs))
    return urlparse.urlunparse(parsed)
