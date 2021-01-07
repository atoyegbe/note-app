from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=40)
    note = models.TextField()

    def __str__(self):
        self.title
