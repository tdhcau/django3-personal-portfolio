from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField()
    text = models.TextField(max_length=250)

    def __str__(self):
        return self.title
