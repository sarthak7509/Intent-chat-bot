# Intent based chatbot
![alt text](https://miro.medium.com/max/1400/1*IfHc0tX71qLedcwJREnf1g.jpeg "credit:-google")
This is an implimentation of intent base chatbot files included are a training file one demo intent json file and a class file of intentbot
## How to use
You can use train.py to train your custom intent file but just check if you have named the file correct and the format of your intent.json file is also correct</br>
Then you can use intentbot.py this file contains a complete withhold class. when passed the path to data.pickle and model path at the time of initilization. You can use its .predict method on you raw text data and it will return both the response and intent</br>
Complete guide to train this model is [here](https://bhatnagarsarthak3.medium.com/intent-based-chatbot-using-tensorflow-f8237f18c0b3)

## Run with Docker
```shell
# 1. First, clone the repo
$ git clone https://github.com/sarthak7509/Intent-chat-bot.git
$ cd intent-chat-bot

# 2. Build Docker image
$ docker build -t intent-chat-bot .

# 3. Run!
$ docker run -it --rm -p 5000:5000 intent-chat-bot
```

## Local Installation

It's easy to install and run it on your computer.

```shell
# 1. First, clone the repo
$ git clone https://github.com/sarthak7509/Intent-chat-bot.git
$ cd keras-flask-deploy-webapp

# 2. Install Python packages
$ pip install -r requirements.txt

# 3. Run!
$ python app.py
```