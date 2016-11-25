from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='static')

class Admin(models.Model):
    username=models.CharField(max_length=12, primary_key=True)
    password=models.CharField(max_length=12)