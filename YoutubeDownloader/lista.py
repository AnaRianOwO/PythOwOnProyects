from pytube import YouTube as Youtube
from tkinter import filedialog

ruta = filedialog.askopenfilename(title = "Sec",filetypes = (("txt files","*.txt"),("all files","*.*")))
archivo = open(ruta, "r")
contenido = archivo.read().splitlines()

def mp3(link):
    video = Youtube(link)
    stream = video.streams.get_audio_only()
    stream.download()
    print("Downloaded "+video.title+" successfully")
    
def principal():
    for i in contenido:
        mp3(i)
        
principal()