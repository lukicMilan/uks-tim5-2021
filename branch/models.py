from django.db import models

from repository.models import Repository

class Branch(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.CharField(max_length=200)
  is_default = models.BooleanField(default=False)
  is_base_of = models.ForeignKey("self", on_delete=models.CASCADE)
  repository = models.ForeignKey(to=Repository, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
