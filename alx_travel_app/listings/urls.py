from django.urls import path, include
from .views import ListingViewSet, BookingViewSet, ReviewViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path(r'', include(router.urls)),
]