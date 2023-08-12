from django.db import models
import requests
from django.conf import settings

class Profile(models.Model):
    user_id = models.CharField(max_length=40, primary_key=True, unique=True, blank=True, default=True)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    full_name = models.CharField(max_length=80, blank=True, null=True)
    #image = models.ImageField(upload_to='image', height_field=None, width_field=None, max_length=100, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.display_name, self.first_name
    
    def save_user_info(self, request):
        sdk_url = settings.ORY_SDK_URL
        sess = requests.get(
            f"{sdk_url}/sessions/whoami",
            cookies=request.COOKIES
        )
    
        traits = sess.json().get('identity', {}).get('traits', None) # dict
        full_name = traits.get('first_name') + " " + traits.get('last_name') # str

        self.first_name = traits.get('first_name')
        self.last_name  = traits.get('last_name')
        self.full_name = full_name
        self.image = traits.get('picture')
        self.email = traits.get('email')
        self.user_id = request.user
        self.save()
        