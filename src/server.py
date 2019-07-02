from flask import Flask
from flask import request
from fanfic_downloader import FanficDownloader
import password
from email_sender import EmailSender

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test", methods=['POST', 'GET'])
def test():
    # return "Taco taco taco" + request.form['url']
    url = request.form['url']
    fic = FanficDownloader("C:/Users/dbarv/PycharmProjects/StupidSummerProject/venv/Scripts/fanficfare.exe ",
                           url,
                           "C:/Users/dbarv/PycharmProjects/StupidSummerProject/build")
    send = EmailSender(password.my_email, password.password, 587, password.kindle_email)
    send.send_fic(fic)
    return 'done'

app.run('localhost', debug=True)
