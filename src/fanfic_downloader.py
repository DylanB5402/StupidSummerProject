import subprocess
import os
import ast

class FanficDownloader:


    def __init__(self, fanficfare_path : str, url : str, file_path : str):
        self.fanficfare_path = fanficfare_path
        self.url = url
        self.file_path = file_path
        self.file_name = ''
        self.get_file_name()

    def get_file_name(self):
        meta_data = subprocess.check_output([self.fanficfare_path, "-f", "mobi", "-m", self.url], cwd=self.file_path).decode('utf-8')
        # print(meta_data)
        meta_data = meta_data[0: meta_data.index('zchapters') - 2] + '}'
        # self.file_name = meta_data[meta_data.index('output_filename') + 19: meta_data.index('publisher') - 6]
        # print(self.file_name)
        json_data = ast.literal_eval(meta_data)
        self.file_name = json_data['output_filename']
        os.remove(self.file_path + '/' + self.file_name)

    def download_story(self):
        print('start download')
        subprocess.call([self.fanficfare_path, "-f", "mobi", self.url],
                        cwd=self.file_path)
        print('downloaded')


