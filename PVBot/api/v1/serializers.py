from rest_framework.serializers import (
    ModelSerializer,
)
from PVBot.models import BotSettings
from PVUser.api.v1.serializers import UserSerializer


class BotSettingsSerializer(ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = BotSettings
        exclude = ['id']
