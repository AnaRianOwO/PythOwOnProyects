from pytube import YouTube, exceptions

link = 'https://youtube.com/clip/UgkxpxznBazYVc6sxqemnKjVy_q3JL5duPRT?si=Nr6oYaFfGMIKU0f0'

try:
    video = YouTube(link)
    stream = video.streams.get_audio_only()
    stream.download(output_path='RUTA_DE_DESCARGA', filename='NOMBRE_DEL_ARCHIVO')
    print("Descarga completada.")
except exceptions.VideoUnavailable:
    print("El video no está disponible. Por favor, verifica el enlace y asegúrate de que el video no sea privado o esté restringido.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")