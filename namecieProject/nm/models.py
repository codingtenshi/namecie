from django.db import models

class Profile(models.Model):
    user_id = models.CharField(max_length=40, primary_key=True, unique=True, blank=True, default=True)
    display_name = models.CharField(max_length=100)
    description = models.TextField()
    # first_name = models.CharField(max_length=20, blank=True, null=True)
    # last_name = models.CharField(max_length=60, blank=True)
    # full_name = models.CharField(max_length=80, blank=True)
    # image = models.ImageField(upload_to='image', height_field=None, width_field=None, max_length=100, null=True)
    # email = models.EmailField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.display_name
    

