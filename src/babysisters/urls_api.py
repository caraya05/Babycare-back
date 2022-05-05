from django.urls import include, path
from rest_framework import routers

from babysisters.viewset.baby_sister_viewset import BabySisterViewSet
from babysisters.viewset.schedule_viewset import ScheduleViewSet

router = routers.DefaultRouter()
router.register(r'baby_sister', BabySisterViewSet, basename='baby_sister')
router.register(r'schedule', ScheduleViewSet, basename='schedule')
urlpatterns = [
    path('', include(router.urls)),
]
