# dgraphclient
Python client for dgrap.io

Within Python use:

dc = dgraphclient('example.com', 8080)  #Add tls=True if you want encryption
my_json_resp = dc.query('your query string')

From command line:

dgraphclient.py --hostname example.com --port 8080 --query 'your query string'


TODO:
Add: Possibility to read query from file in command line mode.
Add: Possibility to use TLS from command line mode.
