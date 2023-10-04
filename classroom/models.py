from django.db import models

# Create your models here.
class room(models.Model):
    name=models.TextField()
    address=models.CharField(max_length=100)
    chat=models.CharField(max_length=500)

    def __str__(self):
        return self.name


