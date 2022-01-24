from django.db import models

class Origin(models.Model):
  name: models.CharField(max_length=50)
  url: models.CharField(max_length=100)
  created = models.DateTimeField()

  def __str__(self):
    return self.name
