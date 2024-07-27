from pytube import YouTube as Youtube
# falta hacer la opcion de descargar varios videos a la vez, podria ser con un 
# archivo txt con los links de los videos a descargar

def mp3(link):
    video = Youtube(link)
    stream = video.streams.get_audio_only()
    stream.download()
    print("Downloaded mp3 successfully")

def mp4(link):
    video = Youtube(link)
    stream = video.streams.get_highest_resolution()
    stream.download()
    print("Downloaded mp4 successfully")
    
def main():
    print("""
    Welcome to Youtube Downloader
    Type the link of the video you want to download""")
    link = input("Link: ")
    print("""
    Type the format you want to download
    1. mp3
    2. mp4""")
    option = input("Option: ")
    if option == "1":
        mp3(link)
    elif option == "2":
        mp4(link)

main()