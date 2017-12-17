from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)
    classifier = models.ForeignKey('Classifier', blank=True, null=True)


    class Meta:
        unique_together = ('name', 'classifier',)

    def __str__(self):
        return self.name
    

class Classifier(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=1000, null=True)
    version =  models.ForeignKey('ClassifierVersion', blank=True, null=True)
    status = models.CharField(max_length=8, default='Не обучен')
    path_to_bin = models.CharField(max_length=100, null=True)


    def save(self, *args, **kwargs):
        
        self.path_to_bin = str(self.name) + '_pickle'
        return super(Classifier, self).save(*args, **kwargs)



    def __str__(self):
        return self.name

    
class ClassifierVersion(models.Model):
    topics = models.ManyToManyField('Topic')
    version = models.IntegerField()
    #путь до файла, с сериализованным объектом
    path_to_bin = models.CharField(max_length=25)

    def __str__(self):
        return self.classifier.name + ' ' + str(version)


