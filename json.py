import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = input('Enter location: ')
if len(url) < 1:
    url ='http://py4e-data.dr-chuck.net/comments_1410046.json'
print('Retrieving', url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

recv = json.loads(data)
info = recv['comments']
print('Count:', len(info))

sum = 0
for item in info:
    sum += item['count']

print('Sum: ', sum)
