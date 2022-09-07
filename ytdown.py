from tkinter import filedialog

from pytube import YouTube
from tkinter import *


def open_window():
    location = filedialog.askdirectory()
    return location


class MyWindow:

    def __init__(self, win):
        check = IntVar()
        btn2 = StringVar()
        # labels
        self.lbl1 = Label(win, text='URL')
        self.lbl2 = Label(win, text='Select download location')
        self.lbl3 = Label(win, text="Audio")
        self.lbl4 = Label(win, text="Video")
        # fields
        self.t1 = Entry(width=50)
        self.checkbox = Checkbutton(win, variable=check)
        self.r2 = Checkbutton(win, variable=btn2)

        self.lbl1.place(x=0, y=20)
        self.t1.place(x=0, y=40)

        self.lbl3.place(x=0, y=80)
        self.checkbox.place(x=50, y=80)

        self.lbl4.place(x=100, y=80)
        self.r2.place(x=150, y=80)
        # buttons
        self.b1 = Button(win, text='Select location and Download', command=self.download)
        self.b1.place(x=50, y=100)

    def download(self):
        # get the variables
        link = self.t1.get()
        downloadLocation = open_window()
        isAudio = self.checkbox.selection_get()

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
window.geometry("300x300")
window.mainloop()
