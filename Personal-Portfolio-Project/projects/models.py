from django.db import models

# Create your models here.
class Project(models.Model):
    #add text field for a title gurl
    title = models.CharField(max_length=75)
    image = models.ImageField(upload_to='images/')
    summary= models.CharField(max_length=400)
    url= models.URLField(max_length=200)

    def __str__(self): #rename objects from projectobehct(1) to summary 
        return self.title