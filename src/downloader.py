from fanfic_downloader import FanficDownloader

# subprocess.call(["fanficfare", "-f", "mobi", "https://www.fanfiction.net/s/12133998/1/A-Patchwork-Knight"], cwd="C:/Users/dbarv/PycharmProjects/OmnibuserToKindle/build")

# result = subprocess.check_output(["fanficfare", "-m", "https://www.fanfiction.net/s/12133998/1/A-Patchwork-Knight"])
# print('687')
# meta_data = result.decode('utf-8')
# print(result.decode('utf-8'))
# print(result[result.index('output_filename'): result.index('publisher')])
# print(meta_data[meta_data.index('output_filename') + 19: meta_data.index('publisher') - 6])

fic = FanficDownloader("C:/Users/dbarv/PycharmProjects/StupidSummerProject/venv/Scripts/fanficfare.exe ", "https://www.fanfiction.net/s/12133998/1/A-Patchwork-Knight", "C:/Users/dbarv/PycharmProjects/StupidSummerProject/build")
fic.download_story()
print(fic.file_name)
