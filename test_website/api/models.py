from django.db import models

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    # image = models.ImageField(upload_to='lecture_images/',
    #                             max_length=255, blank = True, null = True)
    published_date = models.DateTimeField(blank=True, null=True)

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    score = models.IntegerField()

class Test(models.Model):
    question  = models.TextField()
    lecture_id = models.ForeignKey(Lecture, blank=True, null=True, on_delete=models.DO_NOTHING)
    variant_a = models.TextField()
    variant_b = models.TextField()
    variant_c = models.TextField()
    correct_answer = models.TextField()
