import requests

# r = requests.post("https://stupid-summer-project.herokuapp.com/test", {'url' : 'https://www.fanfiction.net/s/10898868/1/Professor-Arc'})
r = requests.post("http://0.0.0.0:33507/test", {'url' : 'https://www.fanfiction.net/s/11237173/1/The-Responsible-One'})
print(r.content.decode('utf-8'))
