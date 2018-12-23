from aip import AipSpeech
from record import main
import os

url = "https://www.google.com/search?q={}"
wav = 'voice.wav'


def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    APP_ID = os.environ['APP_ID']
    API_KEY = os.environ['API_KEY']
    SECRET_KEY = os.environ['SECRET_KEY']

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    main(wav)
    # 识别本地文件
    r = client.asr(get_file_content(wav), 'wav', 16000, {
        'dev_pid': 1536,
    })
    result = r.get("result")

    if result:
        os.system("chrome " + url.format('+'.join(result)))
    else:
        print("未能识别语言")
