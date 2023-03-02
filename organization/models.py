from django.db import models
from django.contrib.auth import get_user_model

from organization.choices import OrganizationCollaboratorRoleChoices

User = get_user_model()


class Organization(models.Model):
    """
        Represent the creator of the content,
        this will contain all the settings to the public creator; url and other stuff will be assigned
        like personal data, lore, info, social networks, etc.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pro = models.BooleanField(default=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class OrganizationCollaborator(models.Model):
    """
        Represent the members of the organization
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, default=OrganizationCollaboratorRoleChoices.ADMIN,
                            choices=OrganizationCollaboratorRoleChoices.choices,
                            help_text='The role of the collaborator in the organization')
    suspended = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(name="unique_organization_collaborator", fields=('organization', 'user'))
        ]

    def __str__(self):
        return f'{self.organization}-{self.user}'
