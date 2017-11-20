#!/usr/bin/python

import requests
import sys
import getopt

class dgraphclient(object):

    def __init__(self, hostname, port, tls=False):
        self._hostname = hostname
        self._port = port
        self._tls = tls
        if self._tls:
            self._conn_string = 'https://'+self._hostname+":"+str(self._port)+'/query?'
        else:
            self._conn_string = 'http://'+self._hostname+":"+str(self._port)+'/query?'

    def query(self, query):
        try:
            resp = requests.post(self._conn_string, data=query)
        except requests.ConnectionError as ce:
            raise ce
        except requests.HTTPError as he:
            raise he
        except requests.Timeout as te:
            raise te
        except requests.TooManyRedirects as re:
            raise re
        else:
            if resp.status_code < 400:
                return resp.json()
            else:
                raise resp.status_code


def main(args):
    _hostname = None
    _port = -1
    _query = None
    dc = None
    options, rem = getopt.gnu_getopt(args, 'h:p:q:f:', ['hostname=', 'port=', 'query=', 'file='])
    for opt, arg in options:
        if opt in ('h', '--hostname'):
            _hostname = arg
        elif opt in ('p', '--port'):
            _port = arg
        elif opt in ('q', '--query'):
            _query = arg

    if _hostname != None and _port > 0:
        dc = dgraphclient(_hostname, _port)
    if _query != None:
        print dc.query(_query)

if __name__ == '__main__':
    main(sys.argv[1:])
