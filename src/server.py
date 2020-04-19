from flask import Flask
from flask import request
from fanfic_downloader import FanficDownloader
# import password
from email_sender import EmailSender
import sys
import os
import threading
from rq import Queue
from worker import conn
import downloader
import password

app = Flask(__name__)
q = Queue(connection=conn)

# my_password = sys.argv[1]
# email = sys.argv[2]
# kindle_email = sys.argv[3]

my_password = password.my_password
email = password.my_email
kindle_email = password.kindle_email

@app.route("/")
def hello():
    # return "Hello World!"
    return "Stupid Summer Project"

@app.route("/hello")
def hi():
    return "hello world"

@app.route("/test", methods=['POST', 'GET'])
def test():
    # return "Taco taco taco" + request.form['url']
    # if (met)
    if request.method == 'POST':
        print('request received')
        url = request.form['url']
        # fic = FanficDownloader("fanficfare", url, "build/")
        # send = EmailSender(email, my_password, 587, kindle_email)
        # send.send_fic(fic)
        # t = threading.Thread(target=download_book(url))
        # t.start()
        q.enqueue(downloader.download_book, url, email, my_password, kindle_email)
        # download_book(url)
    return "done"


# def download_book(url : str):
#     fic = FanficDownloader("fanficfare", url, "build/")
#     # fic.download_story()
#     send = EmailSender(email, my_password, 587, kindle_email)
#     send.send_fic(fic)


# app.run('localhost', debug=True)
if __name__ == '__main__':
    # app.run('0.0.0.0')
    # app.run()
    # print(687)
    # print(password + email + kindle_email)
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port)

