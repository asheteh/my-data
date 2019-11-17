from django.db import models

class Test_1(models.Model):

    question = models.TextField(blank=True)
    a = models.TextField(blank=True)
    b = models.TextField(blank=True)
    c  = models.TextField(blank=True)
    d = models.TextField(blank=True)
    ans = models.TextField(blank=True)
    qtype = models.CharField(max_length=40)



class Score(models.Model):
    qno = models.IntegerField(blank=True,default=1)
    username = models.CharField(blank=True,max_length=120,unique=True)
    score = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)


class Test_2(models.Model):

    question = models.TextField(blank=True)
    a = models.TextField(blank=True)
    b = models.TextField(blank=True)
    c  = models.TextField(blank=True)
    d = models.TextField(blank=True)
    ans = models.TextField(blank=True)
    qtype = models.CharField(max_length=40)



class Score2(models.Model):
    qno = models.IntegerField(blank=True,default=1)
    username = models.CharField(blank=True,max_length=120,unique=True)
    score = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)


