
   
from django.db import models
from django.utils import timezone

from branch.models import Branch
from label.models import Label
from repository.models import Repository

OPENED = "Opened"
CLOSED = "Closed"
MERGED = "Merged"
PULL_REQUEST_STATE = [
    (OPENED, "Opened"),
    (CLOSED, "Closed"),
    (MERGED, "Merged")
]

class Pullrequest(models.Model):
  name = models.CharField(max_length=100)
  status = models.CharField(max_length=20, choices=PULL_REQUEST_STATE, default=OPENED)
  created = models.DateField()
  merge_date = models.DateField(null=True, blank=True)
    
  prRepository = models.ForeignKey(to=Repository, null=True, on_delete=models.CASCADE)

  source_branch = models.ForeignKey(to=Branch, related_name='source_branch', null=True, on_delete=models.CASCADE)
  target_branch = models.ForeignKey(to=Branch, related_name='target_branch', null=True, on_delete=models.CASCADE)
  labels = models.ManyToManyField(Label)

  def __str__(self):
    return self.name
