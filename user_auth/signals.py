from django.contrib.auth.models import User
from .models import Profile

from django.db.models.signals import post_save

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        print('New Profile Created!')

post_save.connect(create_profile, sender=User)