from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from PVBot.models import BotSettings
from .serializers import BotSettingsSerializer


class BotViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = BotSettings.objects.all()
    serializer_class = BotSettingsSerializer
