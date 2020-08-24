from django.db import models

class gallery(models.Model):
    imgtitle = models.CharField(max_length=100)
    imgdesc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

class Image(models.Model):
    title = models.CharField(max_length=200)
    img_tag = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='images/')
