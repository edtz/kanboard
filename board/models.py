from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    members = models.ManyToManyField(User, through="TeamMembership")

class TeamMembership(models.Model):
    user_id = models.ForeignKey(User)
    team_id = models.ForeignKey(Team)

class Project(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(User)
    team_id = models.ForeignKey(Team)

    def __str__(self):
        return self.name

class Sprint(models.Model):
    project_id = models.ForeignKey(Project)
    duration = models.DurationField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return 'Sprint ' + str(self.id)

class Status(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Story(models.Model):
    project_id = models.ForeignKey(Project)
    status_id = models.ForeignKey(Status)
    user_id = models.ForeignKey(User, blank=True)
    sprint_id = models.ForeignKey(Sprint)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description