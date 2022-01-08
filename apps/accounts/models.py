import os
import uuid

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('profile_pic/', filename)


User = get_user_model()
class Profile(models.Model):
    user    = models.OneToOneField(User,on_delete = models.CASCADE)
    name    = models.CharField(max_length=200,blank=True,null=True)
    bio     = models.TextField(max_length=800,blank=True,null=True,help_text="Description of Medical Staff")
    aadhar  = models.CharField(max_length=12,blank=True,null=True)
    phone   = models.CharField(max_length=10,blank=True,null=True)
    image   = models.ImageField(upload_to=get_file_path,blank=True,null=True)
    place   = models.CharField(max_length=200,blank=True,null=True)
    is_medical_staff = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username



@receiver(post_save,sender=User)
def update_profile_signal(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
