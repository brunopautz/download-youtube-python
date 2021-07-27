# PARA CONVERTER EM MP3 É NECESSARIO TER O FFMPEG INSTALADO CNO PATCH DAS VARIAVEIS DO WINDOWS
# LINK DOWNLOAD https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z

# IMPORT LIB
from youtube_dl import YoutubeDL


# FUNCAO DONWLOAD RECEBENDO O URL DO VIDEO
def download(url):
    # OPTIONS DE DOWNLOAD
    audio_downloader = YoutubeDL({
        'outtmpl': 'downloaded_music/%(title)s-%(id)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    })
    while True:
        try:
            print('Youtube Downloader'.center(40, '_'))
            URL = url
            audio_downloader.extract_info(URL)
            return 1
        except Exception:
            print("Couldn\'t download the audio")
            return 0
        finally:
            break


while True:
    url = input("VIDEO: ")
    download(url)
    option = int(input('\n1.download again \n2.Exit\n\nOption here :'))

    if option == 2:
        break
        exit()
    else:
        print(' -------------------------------------- ')