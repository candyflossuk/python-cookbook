"""
This script shows how to access services via HTTP as a client
"""
from urllib import request, parse
import requests

# Base url being accessed
url = "http://httpbin.org/get"

# Dictionary of query params
parms = {"name1": "value1", "name2": "value2"}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a get request and read the response
u = request.urlopen(url + "?" + querystring)
resp = u.read()

# And for a POST

u = request.urlopen(url, querystring.encode("ascii"))

# To supply custom headers - make a dictionary and create a Request instance

headers = {"User-agent": "none/ofyourbusiness", "Spam": "Eggs"}

req = request.Request(url, querystring.encode("ascii"), headers=headers)

# Make a request and read the response
u = request.urlopen(req)
resp = u.read

# If the request is more complex use the requests library - it has useful built in methods
resp = requests.head("http://www.python.org/index.html")

status = resp.status_code
last_modified = resp.headers["last-modified"]
content_type = resp.headers["content-type"]
content_length = resp.headers["content-length"]

# Using requests to login
resp = requests.get(
    "http://pypi.python.org/pypi?:action=login", auth=("user", "password")
)

# Taking cookies from one request to the next ...
resp1 = requests.get(url)
resp2 = requests.get(url, cookies=resp1.cookies)

# And to upload content
url = "http://httpbin.org/post"
files = {"file": ("data.csv", open("data.csv", "rb"))}
r = requests.post(url, files=files)
