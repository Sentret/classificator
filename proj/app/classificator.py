# coding: utf8

import sqlite3 as sq
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from dicttoxml import dicttoxml

import pickle


def data_processing(data):
    data['text'] = [text.lower() for text in data['text']]


def load_data():

    dbname = '../data.sqlite'
    data = [] 
    conn = sq.connect(dbname)
    try:
        c = conn.cursor()
        for row in c.execute('SELECT * FROM data'):
            data.append({'text':row[1],'topic':row[2]})
            
            
    finally:
        conn.close()
    return data



def main():
    # data = load_data()
    # data_processing(data)

    # text_clf = Pipeline([('vect', CountVectorizer()),
    #                  ('tfidf', TfidfTransformer()),
    #                   ('clf', MultinomialNB()),
    #                      ])

    # text_clf.fit(data['text'],data['tag'])


#save
#     filename = 'f1'
#     pkl = open(filename, 'wb')
#     pickle.dump(text_clf, pkl)
# # Close the pickle instances
#     pkl.close()
#LOAD
    pkl = open('f1', 'rb')
    text_clf = pickle.load(pkl)
    #предасказание категории
    docs_new = ['игра закокнчилась со счетом']
    predicted = text_clf.predict(docs_new)
    print(predicted)
    



