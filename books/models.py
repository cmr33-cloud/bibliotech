from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    year_of_release = models.IntegerField()
    publisher = models.CharField(max_length=50)
    genre = models.ExpressionList
    chapters = models.ExpressionList
    