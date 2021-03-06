from django.urls import path, include
from .views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [
    path("", include(router.urls))
]
