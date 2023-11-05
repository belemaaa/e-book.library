from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class Member(AbstractUser):
    profile_image = CloudinaryField('image', folder='', blank=True, null=True)

