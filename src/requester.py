import requests

r = requests.post("http://localhost:5000/test", {'url' : 'https://www.fanfiction.net/s/4536005/1/Oh-God-Not-Again'})
# print(r.content.decode('utf-8'))
