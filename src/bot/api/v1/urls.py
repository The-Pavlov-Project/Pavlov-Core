from rest_framework import routers

from .views import BotViewSet

router = routers.DefaultRouter()
router.register('', BotViewSet)

urlpatterns = [] + router.urls
