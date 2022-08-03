from rest_framework.viewsets import ModelViewSet

from schedule.models import Event
from .serializers import EventSerializer


class EventViewSet(ModelViewSet):
    """Get user calendar"""
    serializer_class = EventSerializer
    queryset = Event.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Event.objects.filter(user=user)
        else:
            return self.queryset
