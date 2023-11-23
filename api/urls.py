from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, CategoryViewSet

router_v1 = DefaultRouter()
router_v1.register('movies', MovieViewSet, basename='movies')
router_v1.register('categories', CategoryViewSet, basename='categories')


app_name = 'api'

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]