from pytube import YouTube as Youtube

url = 'https://www.youtube.com/watch?v=2lAe1cqCOXo&t=14s'
yt = Youtube(url)
print(yt.captions)