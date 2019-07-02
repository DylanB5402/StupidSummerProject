from fanfic_downloader import FanficDownloader
import password
from email_sender import EmailSender


# url = "https://www.fanfiction.net/s/10677106/1/"
url = input('url:')
fic = FanficDownloader("C:/Users/dbarv/PycharmProjects/StupidSummerProject/venv/Scripts/fanficfare.exe ",
                       url,
                       "C:/Users/dbarv/PycharmProjects/StupidSummerProject/build")
send = EmailSender(password.my_email, password.password, 587, password.kindle_email)
send.send_fic(fic)

