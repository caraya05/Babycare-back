from django.urls import include, path
from rest_framework import routers

from bookings.viewset.booking_viewset import BookingViewSet

router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet, basename='booking')
urlpatterns = [
    path('', include(router.urls)),
]
