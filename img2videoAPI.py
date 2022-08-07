
from flask import Flask, request
from img2video import img2video_main
import os
import glob


app = Flask(__name__)


#@app.route('/vid_create',methods = ['POST', 'GET'])
#def vid_create():
 #   if request.method=='GET' :
  #      input_img_path = request.args.get("input_img_path")
   #     print(input_img_path,"-------------")
    #    img2video_main(input_img_path)
     #   return "Hologram Photos creation successful"
@app.route('/vid_create',methods = ['POST', 'GET'])
def vid_create():
    if request.method=='GET' :
        input_img_path = request.args.get("input_img_path")  #holo_op/ give oath with correct "/"
        vid_duration = request.args.get("vid_duration")  #holo_op/#3
        paths = os.listdir(input_img_path)
        print(paths, "=================787")
        for i in paths:
            path = glob.glob(input_img_path + "/" + i + "/*.jpeg")
            print(path,"----42")
            img2video_main(path,vid_duration)
        return "Successful Video Creation"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001,debug = True)