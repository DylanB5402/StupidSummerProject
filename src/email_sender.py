import smtplib
from fanfic_downloader import FanficDownloader
from email.mime import multipart, base
from email import encoders

class EmailSender:

    # port 587
    def __init__(self, email_address : str, password :str, port : int, kindle_email_address : str):
        self.email_address = email_address
        self.password = password
        self.port = port
        self.kindle_email_address = kindle_email_address
        self.email = smtplib.SMTP('smtp.gmail.com', port)
        self.email.ehlo()
        self.email.starttls()
        # password = input('Password:')
        self.email.login(email_address, password)

    def send_fic(self, fic : FanficDownloader):
        msg = multipart.MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = self.kindle_email_address
        msg['Subject'] = ''
        # msg.attach(text.MIMEText('', 'plain'))
        fic.download_story()
        full_path = fic.file_path + '/' + fic.file_name
        attachment = open(full_path, 'rb')
        p = base.MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % fic.file_name)
        msg.attach(p)
        text = msg.as_string()
        self.email.sendmail(self.email_address, self.kindle_email_address, text)
        self.email.quit()


