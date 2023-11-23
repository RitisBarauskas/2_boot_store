from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls', namespace='api')),
    path('', include('movies.urls', namespace='movies')),
]
