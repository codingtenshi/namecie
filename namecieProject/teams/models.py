from django.db import models
from nm.models import Profile

class Teams(models.Model):
    team_name = models.CharField(max_length=50, blank=True, null=True)
    team_description = models.TextField(blank=True, null=True)
    public = False
    admins = models.ForeignKey(Profile,  auto_created=True, on_delete=models.CASCADE)

    # when I use models.ForeignKey I make that one user can be admin in multiple teams 

