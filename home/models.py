from django.db import models

class Contact(models.Model):
    name= models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateTimeField()

class Summarize(models.Model):
    original_text=models.TextField(null=True)
    desc_summary= models.TextField(null=True)
    date_time = models.DateTimeField()

class Generation(models.Model):
    incomp_text=models.TextField(null=True)
    gen_text= models.TextField(null=True)
    date_time = models.DateTimeField()

class Sentiment(models.Model):
    doc_text=models.TextField(null=True)
    sentiment= models.TextField(null=True)
    date_time = models.DateTimeField()

class Question(models.Model):
    con_text=models.TextField(null=True)
    question= models.TextField(null=True)
    answer = models.TextField(null=True)
    date_time = models.DateTimeField()

# Create your models here.
