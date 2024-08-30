from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MessageViewSet

router_v1 = DefaultRouter()

router_v1.register('messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router_v1.urls)),
]