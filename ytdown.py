from pytube import YouTube
from sys import argv

from tkinter import *
class MyWindow:

    link = ''

    def __init__(self, win):
        self.lbl1=Label(win, text='URL')
        self.lbl2=Label(win, text='Download location')
        self.t1=Entry(bd=3)
        self.t2=Entry()

        self.btn1 = Button(win, text='Download')
        self.lbl1.place(x=0, y=50)
        self.t1.place(x=30, y=50)

        self.lbl2.place(x=0, y=100)
        self.t2.place(x=120, y=100)
        self.b1=Button(win, text='Download', command=self.download)

        self.b1.place(x=100, y=150)
    def download(self):
        link=self.t1.get()
        num2=self.t2.get()
        print(self.t1.get())
        print(self.t2.get())


# # link, defined in the terminal command (position 2)
# link = argv[1]
# # download location (position 3)
# downloadLocation = argv[2]
# # download location (position 4)
# whatToDownload = argv[3]
# # creates an object with the link property
# yt = YouTube(link)
#
# #do the magic
# if (whatToDownload == 'a'):
#     print("Downloading--> " + yt.title + " in audio format")
#     file = yt.streams.get_audio_only("mp4")  # audio
#     file.download(downloadLocation)
# elif (whatToDownload == 'v'):
#     print("Downloading--> " + yt.title + " in video format")
#     file = yt.streams.get_highest_resolution()  # video
#     file.download(downloadLocation)
# else:
#     print("Not a valid file type.")
# print("Done!")

window=Tk()
mywin=MyWindow(window)
window.title('YTDownloader')
window.geometry("400x300+10+10")
window.mainloop()

