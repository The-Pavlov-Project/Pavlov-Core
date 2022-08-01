from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Base user model, used to store all user personal informations"""
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    time_zone = models.IntegerField(default=0)
    gender = models.CharField(default='Custom', max_length=100)
    country_code = models.IntegerField(default=0)
    vip_code = models.IntegerField(default=0)
    deep_logging = models.BooleanField(default=True)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username}'


class Creator(models.Model):
    """
        Represent the creator of the content,
        this will contain all the settings to the public creator; url and other stuff will be assigned
        like personal data, lore, info, social networks, etc.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    moderators = models.ManyToManyField(User, related_name='moderators')

    def __str__(self):
        return self.owner.email
