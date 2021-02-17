"""
This script shows how to access services via HTTP as a client
"""
from urllib import request, parse

# Base url being accessed
url = "http://httpbin.org/get"

# Dictionary of query params
parms = {"name1": "value1", "name2": "value2"}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a get request and read the response
u = request.urlopen(url + "?" + querystring)
resp = u.read()
