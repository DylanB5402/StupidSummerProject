from fanfic_downloader import FanficDownloader
import password
from email_sender import EmailSender

fic = FanficDownloader("C:/Users/dbarv/PycharmProjects/StupidSummerProject/venv/Scripts/fanficfare.exe ", "https://www.fanfiction.net/s/12133998/1/A-Patchwork-Knight", "C:/Users/dbarv/PycharmProjects/StupidSummerProject/build")
send = EmailSender(password.my_email, password.password, 587, password.kindle_email)
send.send_fic(fic)

