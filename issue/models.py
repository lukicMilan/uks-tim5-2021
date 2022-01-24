from django.db import models

from pullrequest.models import Pullrequest
from repository.models import Repository
from user.models import User
from milestone.models import Milestone
from label.models import Label
from project.models import Project


class Issue(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=100, default='')
    is_closed = models.BooleanField(default=False)
    opened_by = models.CharField(max_length=50, default='')

    assignee = models.ManyToManyField(User, related_name="assigned_user", blank=True)
    repository = models.ForeignKey(to=Repository, on_delete=models.CASCADE)
    pullrequests = models.ManyToManyField(Pullrequest, blank=True)
    milestones = models.ForeignKey(to=Milestone, on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label, blank=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.issue_title
