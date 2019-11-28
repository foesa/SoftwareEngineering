from django.db import models


class Commit(models.Model):
    repoName = models.CharField(max_length=100,default="None")
    additions = models.IntegerField()
    deletions = models.IntegerField()
    total = models.IntegerField()
    commitDate = models.DateField()
