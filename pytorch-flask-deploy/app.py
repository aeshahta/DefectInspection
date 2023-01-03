# Flask
from unittest import result
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


#Torch
import torch
import torch.nn as nn
import torch.optim as optim
from util import base64_to_pil


# Load and run neural network and make preidction
import copy
import os
from os import walk
import numpy as np
from torchvision import transforms as transforms
from PIL import Image


# Declare a flask app
app = Flask(__name__)
print('Model loaded...')


# Model saved with torch.save(model, 'model.pth')
MODEL_PATH = "./models/model_scripted.pt"
MODEL2_PATH="./models/model2_scripted_defect.pt"


# Load model to detect defect or no 
model1 = torch.jit.load(MODEL_PATH, map_location='cpu')
model1.eval()
# Load model to classify defect type 
model2 = torch.jit.load(MODEL2_PATH, map_location='cpu')
model2.eval()

# check avliable device
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Running on device: {device}")

# Define a function to make prediction
def model_predict(img, model):
    img = img.convert("RGB")
    transform_norm =transforms.Compose([
            transforms.Resize(255),
            #transforms.AutoAugment(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ])
    # get normalized image
    img_normalized = transform_norm(img).float()
    img_normalized = img_normalized.unsqueeze_(0)
    img_normalized = img_normalized.to(device)
    with torch.no_grad():
        model.eval()  
        output =model(img_normalized)
        index = output.cpu().data.numpy().argmax()
        if model == model1:
            classes = ['Good weld', 'Defect']
            class_name = classes[index]
            return class_name 
        if model == model2:
            defect_classes = ['Burn through','Lack of fusion','Misalignment','Lack of penetration']
            defect_class_name = defect_classes[index]
            return defect_class_name           
         
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.json)
        print(len(request.files))
        # Get the image from post request
        img = base64_to_pil(request.json)
        # Make prediction
        result = model_predict(img, model1)
        if result == 'Good weld':
            return jsonify(result=result,probablity=1)
        else:
            result2 = model_predict(img, model2)
            return jsonify(result=result2,probablity=1)

if __name__ == '__main__':
    # serve app on localhost port 5000
    app.run(debug=True)
    # # Serve the app with gevent
    # http_server = WSGIServer(('0.0.0.0', 5000), app)
    # http_server.serv,.e_forever()    

    
