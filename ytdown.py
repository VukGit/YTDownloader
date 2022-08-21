from pytube import YouTube
from sys import argv

# link, defined in the terminal command (position 2)
link = argv[1]
# download location (position 3)
downloadLocation = argv[2]
# download location (position 4)
whatToDownload = argv[3]
# creates an object with the link property
yt = YouTube(link)

#do the magic
if (whatToDownload == 'a'):
    print("Downloading--> " + yt.title + " in audio format")
    file = yt.streams.get_audio_only("mp4")  # audio
    file.download(downloadLocation)
elif (whatToDownload == 'v'):
    print("Downloading--> " + yt.title + " in video format")
    file = yt.streams.get_highest_resolution()  # video
    file.download(downloadLocation)
else:
    print("Not a valid file type.")
print("Done!")
