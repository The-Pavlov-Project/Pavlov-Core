from django.db import models
from organization.models import Organization


class Rule(models.Model):
    """
        Rules for the organization
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rule = models.TextField()
    mandatory = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'


class ModeratorsRule(Rule):
    """Rules to follow for the moderators"""


class OrganizationRule(Rule):
    """Rules for the members of the organization"""
