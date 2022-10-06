import os
from pytube import YouTube
from tkinter import *
from tkinter import messagebox

YLOG = os.environ.get('YOUTUBE_LOG1')
YPASS = os.environ.get('YOUTUBE_PASS1')


# def download_video():
#     download_location = 'D:/YT_DWLD'
#     video_address = url_input.get()
#     if len(video_address) == 0:
#         messagebox.showinfo(title="Blank entry.", message="Input video address.")
#     else:
#         is_okay = messagebox.askokcancel(title=video_address, message=f"Video address is: {video_address}\n")
#
#         if is_okay:
#             yt = YouTube(video_address, use_oauth=True, allow_oauth_cache=True)
#             yt.streams.filter(progressive=True)
#             print(yt.streams.order_by('resolution'))
#             yt.streams.get_highest_resolution().download(download_location)
#             url_input.delete(0, END)
#             messagebox.showinfo(title="Download finished", message=f"Video: {yt.title} is finished.")
#
#
# window = Tk()
# window.title("Version MK1")
# window.minsize(width=1000, height=500)
#
# # Labels
# link = Label(text="Video URL")
# link.grid(column=1, row=0)
#
# # Buttons
# download_button = Button(text="Download", command=download_video)
# download_button.grid(column=1, row=1)
#
# # Entry
# url_input = Entry(width=20)
# url_input.grid(column=2, row=0)
# url_input.focus()
#
#
# window.mainloop()


""""""

video_url = ""
download_location = 'D:/YT_DWLD'

yt = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
yt.streams.filter(progressive=True)

print(yt.streams.order_by('resolution'))
yt.streams.get_highest_resolution().download(download_location)

# yt.streams.get_by_itag('22').download(download_location)
