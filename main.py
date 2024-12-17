import yt_dlp

link = input("ENter link to download:")
options = {
    'format':'best',
    'outtmpl':'download.mp4'
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([link])

print("Downlaod Finished......")
