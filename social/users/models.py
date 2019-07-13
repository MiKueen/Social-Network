from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  description = models.CharField(max_length=100,default='')
  city = models.CharField(max_length=20, default='')
  state = models.CharField(max_length=20, default='')
  country = models.CharField(max_length=20, default='')
  website = models.URLField(default='')
  phone = models.IntegerField(default=0)
  image = models.ImageField(upload_to='profile_image', blank=True)

  def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
  #follows = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by', symmetrical=False)

#User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])