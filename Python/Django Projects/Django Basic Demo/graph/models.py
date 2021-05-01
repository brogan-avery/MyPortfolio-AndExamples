from django.db import models

class Element_levels(models.Model):
    Ba = models.FloatField()
    Zr = models.FloatField()
    Sr = models.FloatField()
    Rb = models.FloatField()
    Zn = models.FloatField()
    Ni = models.FloatField()
    Fe = models.FloatField()
    Mn = models.FloatField()
    Ti = models.FloatField()
    Ca = models.FloatField()
    K = models.FloatField()

class Temps(models.Model):
    date = models.CharField(max_length=30)
    temp = models.FloatField()

class Scores(models.Model):
    rank = models.IntegerField()
    region = models.CharField(max_length=400)
    score = models.FloatField()
