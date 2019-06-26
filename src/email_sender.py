import smtplib
from fanfic_downloader import FanficDownloader
class EmailSender:

    # port 587
    def __init__(self, email_address : str, password :str, port : int):
        self.email = smtplib.SMTP('smtp.gmail.com', port)
        self.email.ehlo()
        self.email.starttls()
        # password = input('Password:')
        self.email.login(email_address, password)

    # def send_fic(self, fic : FanficDownloader):
        