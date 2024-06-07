import moviepy.editor # moviepy is a module used for video editing.
from tkinter.filedialog import * # tkinter is used to open video file from device

vid = askopenfilename() # Opening the file from device
video = moviepy.editor.VideoFileClip(vid) 

aud = video.audio # Video is converted to audio
aud.write_audiofile("demo.mp3")

print("----END----")