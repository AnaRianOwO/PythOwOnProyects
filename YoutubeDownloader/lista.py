from pytube import YouTube as Youtube
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import os

ruta = filedialog.askopenfilename(title = "Sec",filetypes = (("txt files","*.txt"),("all files","*.*")))
archivo = open(ruta, "r")
contenido = archivo.read().splitlines()
folder = filedialog.askdirectory(title = "Select folder to save the files")

def download(link, folder="C:/Users/Usuario/Music"):
    video = Youtube(link)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path=folder)
    print("Downloaded "+video.title+" successfully")

def principal():
    for i in contenido:
        download(i, folder)
        tomp3(folder)
        
def tomp3(folder):
    for archivo in os.listdir(folder):
        if archivo.endswith(".mp4"):
            ruta_completa = os.path.join(folder, archivo)
            video = VideoFileClip(ruta_completa)
            video.audio.write_audiofile(os.path.join(folder, archivo[:-4] + ".mp3"))
            video.close()
            os.remove(ruta_completa)
principal()