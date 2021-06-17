import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import werkzeug
import pickle
import json
import numpy as np
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask import Flask
from intentbot import intentBot

model2 = None
app = Flask(__name__)

CORS(app)

with open("intent-bot-data/intent.json") as file:
    data = json.load(file)

with open("intent-bot-data/outputs/data.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)

path = "intent-bot-data/bot_model"

def getmodel():
    global model2
    model2 = intentBot(json_data=data,words=words,labels=labels,training=training,output=output,model_Path=path)

getmodel()
#this code initialize the model to start predicting
print(model2.predict("hello"))


@app.route("/intent",methods=['POST'])
def intents():
    message = request.get_json(force=True)
    data = str(message["question"])
    print(data)
    response, intent = model2.predict(data)
    reply = {
        "reply":response,
        "intent": intent
    }
    print(reply)
    return jsonify(reply)

@app.route("/")
def index():
    return "<h1>Hello</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
