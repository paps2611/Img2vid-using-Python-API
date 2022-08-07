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
            img2vid_main(path,vid_duration)
        return "Successful Video Creation"