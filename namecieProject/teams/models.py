from django.db import models
from nm.models import Profile

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    team_description = models.TextField(blank=True, null=True)
    public = models.BooleanField(default=False)
    year_founded = models.IntegerField(blank=True, null=True)

    members = models.ManyToManyField(Profile, related_name='teams_member', blank=True)
    admins = models.ManyToManyField(Profile, related_name='teams_admin', blank=True)
    moderators = models.ManyToManyField(Profile, related_name='teams_moderator', blank=True)