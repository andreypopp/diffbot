"""

    diffbot -- diffbot API
    ======================

    >>> api = DiffBot('<my api token>')
    >>> api.article('http://google.com', summary=True)
    {...}

"""

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

    def _json_request(self, url, data):
        if not 'token' in data:
            data['token'] = self.token
        r = self.pool.request('GET', url, data)
        return json.loads(r.data)

    def article(self, url, **params):
        """ Process ``url`` as an article"""
        data = {'url': url}
        data.update(params)
        return self._json_request(self.API_ARTICLE, data)

    def frontpage(self, url, **params):
        """ Process ``url`` as a frontpage"""
        data = {'url': url}
        data.update(params)
        return self._json_request(self.API_FRONTPAGE, data)
