import requests

r = requests.post("https://stupid-summer-project.herokuapp.com/test", {'url' : 'https://www.fanfiction.net/s/10898868/1/Professor-Arc'})
print(r.content.decode('utf-8'))
