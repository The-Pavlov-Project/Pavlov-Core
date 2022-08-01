from rest_framework.viewsets import ModelViewSet

from schedule.models import Event
from .serializers import EventSerializer


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.none()
    """Get user calendar"""

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)
