from flask import Flask
from flask import request
from fanfic_downloader import FanficDownloader
# import password
from email_sender import EmailSender
import sys
import os

app = Flask(__name__)

password = sys.argv[1]
email = sys.argv[2]
kindle_email = sys.argv[3]

# password = password.password
# email = password.my_email
# kindle_email = password.kindle_email

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
        url = request.form['url']
        fic = FanficDownloader("fanficfare", url, "/build")
        send = EmailSender(email, password, 587, kindle_email)
        send.send_fic(fic)
    return "done"

# app.run('localhost', debug=True)
if __name__ == '__main__':
    # app.run('0.0.0.0')
    # app.run()
    # print(687)
    # print(password + email + kindle_email)
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port)

