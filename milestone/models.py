from django.db import models
from django.utils import timezone

from datetime import datetime, timezone
from project.models import Project
from repository.models import Repository

class Milestone(models.Model):
  title = models.CharField(max_length=50, default='')
  description = models.TextField(default='', blank= True)
  is_closed = models.BooleanField(default=False)
  created = models.DateField(auto_now_add=True)
  due_date = models.DateField(null=True, blank=True)

  project = models.ForeignKey(to=Project, null=True, on_delete=models.CASCADE)
  repository = models.ForeignKey(to=Repository, null=True, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
