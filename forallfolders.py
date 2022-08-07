import glob
import numpy
import cv2 as cv
import moviepy.editor as mp

# adding images
clip = []
path = glob.glob("C:/Pratyush/Task1 using API/Alphabet/A/*.jpeg")
for img in path:
    clip.append(mp.ImageClip(img).set_duration(3))

# concatenating images
video = mp.concatenate_videoclips(clip, method='compose')
video.write_videofile("C:/Pratyush/Task1 using API/Alphabet/A/ouput.mp4", threads=16, fps=1, remove_temp=True, codec="libx264", audio_codec="aac")


# adding images
clip = []
path = glob.glob("C:/Pratyush/Task1 using API/Alphabet/B/*.jpeg")
for img in path:
    clip.append(mp.ImageClip(img).set_duration(3))

# concatenating images
video = mp.concatenate_videoclips(clip, method='compose')
video.write_videofile("C:/Pratyush/Task1 using API/Alphabet/B/ouput.mp4", threads=16, fps=1, remove_temp=True, codec="libx264", audio_codec="aac")


# adding images
clip = []
path = glob.glob("C:/Pratyush/Task1 using API/Alphabet/C/*.jpeg")
for img in path:
    clip.append(mp.ImageClip(img).set_duration(3))

# concatenating images
video = mp.concatenate_videoclips(clip, method='compose')
video.write_videofile("C:/Pratyush/Task1 using API/Alphabet/C/ouput.mp4", threads=16, fps=1, remove_temp=True, codec="libx264", audio_codec="aac")



# adding images
clip = []
path = glob.glob("C:/Pratyush/Task1 using API/Alphabet/D/*.jpeg")
for img in path:
    clip.append(mp.ImageClip(img).set_duration(3))

# concatenating images
video = mp.concatenate_videoclips(clip, method='compose')
video.write_videofile("C:/Pratyush/Task1 using API/Alphabet/D/ouput.mp4", threads=16, fps=1, remove_temp=True, codec="libx264", audio_codec="aac")
