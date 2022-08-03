from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('manage', views.EventViewSet)
router.register('public', views.EventViewSet)

urlpatterns = router.urls
