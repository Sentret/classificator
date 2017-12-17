from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from app.models import Classifier
from app.models import Topic
from django.views.generic.edit import *
from django.views.generic.list import ListView
from app.forms import ClassifierForm
from django.views.decorators.csrf import csrf_exempt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import app.classificator
import xml.etree.ElementTree as XMLElementTree
import pickle

def main(request):
    classifiers = Classifier.objects.all()
    return render(request,'app/main.html',context={'classifiers':
                                                    classifiers})


class ClassifierCreateView(CreateView):
    model = Classifier
    form_class = ClassifierForm

    def get_success_url(self):
        return reverse('main')



def ClassifierInfoView(request, pk):
    topics = Topic.objects.filter(classifier__id = pk)
    return render(request,'app/classifier_info.html',context={'topics':
                                                    topics,'classifier_pk':pk})



@csrf_exempt
def api_train(request, pk):

    classifier = get_object_or_404(Classifier,pk=pk)

    root = XMLElementTree.fromstring(request.body)
    topics = []
    data = {'text':[],'topic':[]}

    for child in root:
        data['text'].append(child[0].text)
        data['topic'].append(child[1].text)

        if child[1].text not in topics:
            topics.append(child[1].text)


    text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                      ('clf', MultinomialNB()),
                         ])

    text_clf.fit(data['text'],data['topic'])

    filename = classifier.path_to_bin
    pkl = open(filename, 'wb')
    pickle.dump(text_clf, pkl)
    pkl.close()

    classifier.status = 'Обучен'
    classifier.save()

    #если переобучаем модель, обновляем список тематик
    Topic.objects.filter(classifier = classifier).delete()


    for topic in topics:
        Topic.objects.create(name=topic, classifier=classifier)

    return HttpResponse(status=200)
    


@csrf_exempt
def api_classify(request, pk):


    classifier = get_object_or_404(Classifier,pk=pk)

    pkl = open(classifier.path_to_bin, 'rb')
    text_clf = pickle.load(pkl)

    root = XMLElementTree.fromstring(request.body)

    data = []
    for child in root:
        data.append({'text':child.text,'topic':text_clf.predict([child.text])[0]})
    
    respose = '<response>\n'
    for entry in data:
        respose +='<item>\n'
        respose += '   <text>' + entry['text'] + '</text>\n'
        respose += '   <topic>' + entry['topic'] + '</topic>\n' 
        respose +='<item>\n'


    respose +='</response>\n'   
    return HttpResponse(respose)
   

@csrf_exempt
def classify(request, pk):

    classifier = get_object_or_404(Classifier,pk=pk)

    pkl = open(classifier.path_to_bin, 'rb')
    text_clf = pickle.load(pkl)
    topic = text_clf.predict([request.body.decode('utf-8')])[0]
     
    return HttpResponse(topic)
