from __future__ import absolute_import
from __future__  import division
from __future__ import print_function
import tensorflow as tf
import numpy as np
from skimage.io import imread
from skimage.transform import resize
import cv2
import numpy as np
import os
from reader import *
from flask import Flask , request , jsonify
from PIL import Image
from io import BytesIO
import time



graph = tf.compat.v1.get_default_graph()
#model22._make_predict_function()

app = Flask("main-fight")

@app.route('/api/fight/',methods= ['GET','POST'])
def main_fight(accuracyfight=0.91):
    with graph.as_default():
    #with tf.Graph().as_default():

        np.random.seed(1234)
        model22 = fight(tf)

        aman = {}
        # if os.path.exists('./tmp.mp4'):
        #     os.remove('./tmp.mp4')
        #filev = request.files['file']
        # file = open("tmp.mp4", "wb")
        # file.write(filev.read())
        # file.close()
        vid = reader(cv2,"hdfight.mp4")
        datav = np.zeros((1, 30, 160, 160, 3), dtype=np.float)
        datav[0][:][:] = vid
        millis = int(round(time.time() * 1000))


        f , precent = pred_fight(model22,datav,acuracy=0.65)

        aman = {'fight':f , 'percentegeoffight':str(precent)}

        millis2 = int(round(time.time() * 1000))
        aman['processing_time'] =  str(millis2-millis)
        resnd = jsonify(aman)
        resnd.status_code = 200
        print('value is:',aman)
        return resnd


app.run(host='0.0.0.0',port=5000)
