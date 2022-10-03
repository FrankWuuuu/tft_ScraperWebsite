from django.db import models

# Create your models here.
class CarryAndComps (models.Model):
  body = models.TextField()

  def __str__(self):
    return self.body[0:50]