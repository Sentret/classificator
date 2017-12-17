from django.conf.urls import url
from django.contrib import admin
from app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main, name='main'),
    url(r'^/create', views.ClassifierCreateView.as_view(), name='classifier-create'),
    url(r'^classifiers/(?P<pk>\d+)/info/$', views.ClassifierInfoView, name='classifier-info'),
    url(r'^classifiers/(?P<pk>\d+)/api_train/$', views.api_train),
    url(r'^classifiers/(?P<pk>\d+)/api_classify/$', views.api_classify),
    url(r'^classifiers/(?P<pk>\d+)/classify/$', views.classify, name='classify')

]
