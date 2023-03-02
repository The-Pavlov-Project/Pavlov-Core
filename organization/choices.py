from django.db import models
from django.utils.translation import gettext_lazy as _


class OrganizationCollaboratorRoleChoices(models.TextChoices):
    """Organization Collaborator Role choices"""
    ADMIN = 'admin', _('Administrator')
    MODERATOR = 'moderators', _('Moderators')
    EDITOR = 'editor', _('Editor')
