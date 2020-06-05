from django.db import models

# Create your models here.

class Imagens(models.Model):
    imagem =  models.TextField()
    data = models.DateTimeField(auto_created=True)