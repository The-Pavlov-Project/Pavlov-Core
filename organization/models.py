from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Organization(models.Model):
    """
        Represent the creator of the content,
        this will contain all the settings to the public creator; url and other stuff will be assigned
        like personal data, lore, info, social networks, etc.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    managers = models.ManyToManyField(User, related_name='managers')

    def __str__(self):
        return f'{self.name}'
