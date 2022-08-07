import glob
import numpy
import cv2 as cv
import moviepy.editor as mp

#def adding_img():
  #  for img in path:
     #  clip.append(mp.ImageClip(img).set_duration(3))

def img2video_main(folder_path,vid_duration):
    clip = []
    # folder_path = glob.glob(path+"/*.jpeg")
    for img in folder_path:
        clip.append(mp.ImageClip(img).set_duration(int(vid_duration)))
    video = mp.concatenate_videoclips(clip, method='compose')
    video.write_videofile("Alphabet/Final_video.mp4", threads=16, fps=1, remove_temp=True,
                          codec="libx264", audio_codec="aac")
    return "succesful"
#clip = []
#path = glob.glob("Alphabet/test/*.jpeg")
#adding_img()
#img2video_main()