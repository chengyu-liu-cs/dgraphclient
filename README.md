# dgraphclient
Python client for dgraph.io<br>

Within Python use:

dc = dgraphclient('example.com', 8080) <br>
#Add tls=True if you want encryption<br>
my_json_resp = dc.query('your query string')<br>

From command line:

dgraphclient.py --hostname example.com --port 8080 --query 'your query string'


TODO:<br>
Add: Possibility to read query from file in command line mode.<br>
Add: Possibility to use TLS from command line mode.<br>
