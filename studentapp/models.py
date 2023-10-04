from django.db import models

class Students(models.Model):
    Name=models.CharField(max_length=50,unique=True)
    div=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    roll_number=models.CharField(max_length=50)


def room():
    return None