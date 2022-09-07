import ssl
import certifi
from pytube import YouTube
from tkinter import *


class MyWindow:

    def __init__(self, win):
        btn1 = StringVar()
        btn2 = StringVar()
        # labels
        self.lbl1 = Label(win, text='URL')
        self.lbl2 = Label(win, text='Download location')
        self.lbl3 = Label(win, text="Audio")
        self.lbl4 = Label(win, text="Video")
        # fields
        self.t1 = Entry()
        self.t2 = Entry()
        self.r1 = Radiobutton(win, variable=btn1)
        self.r2 = Radiobutton(win, variable=btn2)

        self.lbl1.place(x=0, y=20)
        self.t1.place(x=0, y=40)

        self.lbl2.place(x=0, y=80)
        self.t2.place(x=0, y=100)

        self.lbl3.place(x=0, y=150)
        self.r1.place(x=50, y=150)

        self.lbl4.place(x=100, y=150)
        self.r2.place(x=150, y=150)
        # buttons
        self.b1 = Button(win, text='Download', command=self.download)
        self.b1.place(x=50, y=200)

    def download(self):
        # get the variables
        link = self.t1.get()
        downloadLocation = self.t2.get()
        isAudio = self.r1

        # main logic
        yt = YouTube(link)
        if isAudio:
            print("Downloading--> " + yt.title + " in audio format")
            file = yt.streams.get_audio_only("mp4")
            file.download(downloadLocation)
        else:
            print("Downloading--> " + yt.title + " in video format")
            file = yt.streams.get_highest_resolution()  # video
            file.download(downloadLocation)
        print("Done!")


window = Tk()
mywin = MyWindow(window)
window.title('YTDownloader')
window.geometry("400x300+10+10")
window.mainloop()
