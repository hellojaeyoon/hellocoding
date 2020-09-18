from django.db import models

# Create your models here.
class Review(models.Model):

    class Scores(models.IntegerChoices):
        A = 5
        B = 4
        C = 3
        D = 2
        F = 1
        
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    rank = models.IntegerField(choices=Scores.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title