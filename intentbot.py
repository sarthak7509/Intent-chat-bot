import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
NLTK_DIR = "punkt"
os.environ['NLTK_DATA'] = NLTK_DIR
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy as np
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import random
import json
import pickle
class intentBot:
    def __init__(self, json_data, words, labels, training, output, model_Path):
        super(intentBot, self).__init__()
        self.data = json_data
        self.words = words
        self.labels = labels
        self.training = training
        self.output = output
        print("[+]loading models")
        self.model = tf.keras.models.load_model(model_Path)
        print("[+]model loaded")

    def _bag_of_words(self, s, words):
        bag = [0 for _ in range(len(words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1
        return np.array(bag)

    def predict(self, sentence):
        bag = [self._bag_of_words(sentence, self.words)]
        bag = np.asarray(bag)
        results = self.model.predict(bag)
        result_index = np.argmax(results)
        tag = self.labels[result_index]

        for tg in self.data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        response = random.choice(responses)
        return response, tag

if __name__ == '__main__':
    with open("intent-bot-data/intent.json") as file:
        data = json.load(file)

    with open("intent-bot-data/outputs/data.pickle","rb") as f:
        words, labels, training, output = pickle.load(f)

    path = "intent-bot-data/bot_model"
    bot = intentBot(json_data=data,words=words,labels=labels,training=training,output=output,model_Path=path)
    
    question = input("What you wanna ask me?:- ")

    response,intent = bot.predict(question)
    print(response)
    print(intent)