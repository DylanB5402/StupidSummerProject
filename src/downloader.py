from fanfic_downloader import FanficDownloader
import password
from email_sender import EmailSender
import subprocess
import  json
import  ast

fanficfare_path = 'C:/Users/dbarv/PycharmProjects/StupidSummerProject/venv/Scripts/fanficfare.exe'
file_path = "C:/Users/dbarv/PycharmProjects/StupidSummerProject/build"

# url = "https://www.fanfiction.net/s/10677106/1/"
url = input('url:')
# url = 'https://www.fanfiction.net/s/11762850/1/Harry-Potter-and-the-Accidental-Horcrux'
fic = FanficDownloader("C:/Users/dbarv/PycharmProjects/StupidSummerProject/venv/Scripts/fanficfare.exe",
                       url,
                       "C:/Users/dbarv/PycharmProjects/StupidSummerProject/build")
send = EmailSender(password.my_email, password.password, 587, password.kindle_email)
send.send_fic(fic)

# meta_data = str(subprocess.check_output([fanficfare_path, "-f", "mobi", "-m", url], cwd=file_path).decode('utf-8'))
# # meta_data = meta_data.replace("'", "\"")
# meta_data = meta_data[0: meta_data.index('zchapters') - 2] + '}'
# print(meta_data)
# # json_data = json.loads(meta_data)
# json_data = ast.literal_eval(meta_data)
# print(json_data['output_filename'])
# print(json_data['title'] + '-json_data[])
