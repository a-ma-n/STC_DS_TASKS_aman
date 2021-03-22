import base64
import numpy as np
import io
from PIL import Image
import keras
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask

app=Flask(__name__)

def get_model():
    global model
    model=load_model('VGG16_cats_and_dogs.h5')
    print(" * Model loaded!")

def preprocess_image(image,target_size):
    if image.mode !="RGB":
        image=image.convert("RGB")
    image=image.resize(target_size)
    image=img_to_array(image)#convert the image to a numpy array and then expanfd its dimensions
    image=np.expand_dims(image,axis=0)

    return image

print(" * Loading keras model...")
get_model()

@app.route("/predict",methods=["POST"])
def predict():
    message=request.get_json(force=True)
    encoded=message['image']#assign the value of key associated to image from json data to message
    #base 64 encoded image sent by the client we decode it then
    decoded=base64.b64decode(encoded)
    image=Image.open(io.BytesIO(decoded))
    #open in image file ,data stored within the decoded variables as bytes and not in actula file so we wra[ it into a image file and pass that into open]
    #set itequal to instance of pil image
    processed_image=preprocess_image(image,target_size=(224,224))

    prediction=model.predict(processed_image).tolist()
    #predict returns a numpy array with the predictions  convert it to list for it tomake jsonify call

    response={
     'prediction':
     {
     'dog':prediction[0][0],
     'cat':prediction[0][1]
     }
    }
    return jsonify(response)
