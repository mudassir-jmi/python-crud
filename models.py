from django.db import models

# Create your models here.
class todo(models.Model):
  text=models.CharField(max_length=200)
  added_date=models.DateField()
