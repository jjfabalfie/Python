# This is the same as the original pytube script but Iv'e implemented Tkinter into it for people who prefer a GUI instead of terminal work.
# To run this script run pip install Tk and pip install pytube
from tkinter import *
from pytube import *
from tkinter import filedialog
def download_video():
    try:
        # Create a YouTube object
        yt = YouTube(url.get())
        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(downloadpath.get())
        filedialog.askopenfilename(initialdir=downloadpath.get())
    except Exception as e:
        print("Error: {}".format(str(e)))

def submit():
    download_video()
def clear():
    url.delete(0,END)
    downloadpath.delete(0,END)
root = Tk()

frame_heading = Frame(root)
frame_heading.grid(row=0, column=0, columnspan=2, padx=30, pady=5)
frame_entry = Frame(root)
frame_entry.grid(row=1, column=0, columnspan=2, padx=25, pady=10)

root.title("PYtube")

Label(frame_heading, text="Youtube Video Downloader", font=('Arial',16))\
    .grid(row=0, column=0, padx=0, pady=5)

Label(frame_entry, text="Youtube URL: ")\
    .grid(row=0, column=0, padx=0, pady=5)
url = Entry(frame_entry, width= 15, bg = "white")
url.grid(row=0, column=1, padx=5, pady=5)

Label(frame_entry, text="Exact Output Path: ")\
    .grid(row=1, column=0, padx=0, pady=5)
downloadpath = Entry(frame_entry, width= 15, bg = "white")
downloadpath.grid(row=1, column=1, padx=5, pady=5)

submit_button = Button(root, text="Submit", width=7, command=submit)
submit_button.grid(row=2, column=0, padx=0, pady=5)

clear_button = Button(root, text="Clear", width=7, command=clear)
clear_button.grid(row=2, column=1, padx=0, pady=5)

root.mainloop()
