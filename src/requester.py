import requests

r = requests.post("http://localhost:5000/test", {'url' : 'https://www.fanfiction.net/s/11762850/1/'})
# print(r.content.decode('utf-8'))
