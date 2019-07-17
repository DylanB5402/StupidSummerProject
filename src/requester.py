import requests

r = requests.post("https://stupid-summer-project.herokuapp.com/test", {'url' : 'https://www.fanfiction.net/s/8525320/1/Oh-You-Didn-t-Know-Yeah-He-s-Awesome'})
# r = requests.post("http://0.0.0.0:33507/test", {'url' : 'https://www.fanfiction.net/s/8525320/1/Oh-You-Didn-t-Know-Yeah-He-s-Awesome'})
print(r.content.decode('utf-8'))
