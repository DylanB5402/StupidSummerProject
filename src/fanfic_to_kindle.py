from fanfic_downloader import FanficDownloader
from email_sender import EmailSender
import config
import sys

# url = sys.argv[1]
url = "https://www.fanfiction.net/s/7340362/1/Drapple"
my_password = config.my_password
email = config.my_email
kindle_email = config.kindle_email
fanficfare_path = config.fanficfare_path
output_path = config.output_path

fic = FanficDownloader(fanficfare_path,
                       url, output_path)
send = EmailSender(email, my_password, 587, kindle_email)
send.send_fic(fic)