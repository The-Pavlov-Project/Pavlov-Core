import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


from organization.models import Organization

User = get_user_model()


class Metadata(models.Model):
    """
    Metadata model
    """
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(Metadata):
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    private = models.BooleanField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class EventDiscord(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=False, help_text='If the event has been sent to discord')

    # event_id = models.CharField(max_length=200)
    channel_id = models.CharField(max_length=200, null=True, blank=True)
    creator_id = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def publish_event(self):
        requests.post(
            f'{settings.URI_DISCORD_BOT_API}/api/event/create',
            data={
                # 'event_id': self.event_id
            }
        )
        self.is_published = True
        self.save()

    def __str__(self):
        return self.event_id
