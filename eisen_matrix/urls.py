from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("frontend.urls")),
    path('users/', include("auth-api.urls")),
    path('admin/', admin.site.urls),
]
