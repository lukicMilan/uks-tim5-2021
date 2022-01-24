from re import T
from django.db import models

from django.contrib.auth.models import User
from origin.models import Origin


class Repository(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  created = models.DateTimeField()
  is_private = models.BooleanField(default=True)

  owner = models.ForeignKey(User, null=True, related_name='user_owner', on_delete=models.CASCADE)
  collaborate = models.ManyToManyField(User, related_name='user_collaborate')
  origin = models.ManyToManyField(Origin)

  def __str__(self):
    return self.name
