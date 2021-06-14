import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import tensorflow as tf

tf.get_logger().setLevel('ERROR')
import json
import pickle

with open('intent.json') as f:
    data = json.load(f)
words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])
    if intent['tag'] not in labels:
        labels.append(intent['tag'])
# print(words)
# print(labels)
# print(doc_x)
# print(doc_y)

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []
out_empty = [0 for _ in range(len(labels))]
for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)
training = np.array(training)
output = np.array(output)
print(len(training[0]))
# print(output)
with open("Outputs/data.pickle", "wb") as f:
    pickle.dump((words, labels, training, output), f)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(training[0]),), activation="relu"))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(output[0]), activation='softmax'))

sgd = tf.keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', metrics=["accuracy"], optimizer=sgd)
print(model.summary())

history = model.fit(training, output, epochs=200, batch_size=8)
model.save("bot_model")
