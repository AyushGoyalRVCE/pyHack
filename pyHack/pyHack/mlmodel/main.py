from math import ceil
from tabnanny import verbose
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


def run():
    filepath = r'C:\Users\DELL\Desktop\Ajay\Text classification\sentiment labelled sentences\feedbacks.txt'
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    sentences = df['sentence'].values
    y = df['label'].values
    sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)

    vectorizer = CountVectorizer(min_df=0, lowercase=False)
    vectorizer.fit(sentences_train)
    x_train = vectorizer.transform(sentences_train)
    x_test = vectorizer.transform(sentences_test)

    classifier = LogisticRegression()
    classifier.fit(x_train, y_train)
    score = classifier.score(x_test, y_test)

    tokenizer = Tokenizer(num_words=500)
    tokenizer.fit_on_texts(sentences_train)
    x_train = tokenizer.texts_to_sequences(sentences_train)
    x_test = tokenizer.texts_to_sequences(sentences_test)
    vocab_size = len(tokenizer.word_index) + 1

    maxlen = 100
    x_train = pad_sequences(x_train, padding='post', maxlen=maxlen)
    x_test = pad_sequences(x_test, padding='post', maxlen=maxlen)

    embedding_dim = 50

    model = Sequential()
    model.add(layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=maxlen))
    model.add(layers.Conv1D(128, 5, activation='relu'))
    model.add(layers.GlobalMaxPool1D())
    model.add(layers.Dense(10, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(x_train, y_train, epochs=20, verbose=False, validation_data=(x_test, y_test), batch_size=10)
    loss, accuracy = model.evaluate(x_train, y_train, verbose=False)
    print(loss, accuracy)
    loss, accuracy = model.evaluate(x_test, y_test, verbose=False)
    print(loss, accuracy)
    model.save_weights('model.h5')
    s = 0
    c = 0
    print("Enter your review")
    while True:
        st = input()
        if (st == ""):
            break
        l = []
        l.append(st)
        test = tokenizer.texts_to_sequences(l)
        test = pad_sequences(test, padding='post', maxlen=maxlen)
        l = model.predict(test)
        print(ceil(l[0][0] * 5))
        s = s + ceil(l[0][0] * 5)
        c = c + 1
    print(s / c)


run()