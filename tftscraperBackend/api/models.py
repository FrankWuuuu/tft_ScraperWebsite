from django.db import models

# Create your models here.
class CarryAndComps (models.Model):
  name = models.CharField(max_length = 200)
  body = models.JSONField()


  def __str__(self):
    return self.name
    