from django.db import models
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Movies(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    rel_date = models.DateTimeField()
    genre = models.ForeignKey(Genre, default=1)

    def __str__(self):
        return self.name

    

# Create your models here.
