from rest_framework.routers import DefaultRouter
from django.urls import path, include

from app.views import MessageModelViewSet

router = DefaultRouter()
router.register('message',MessageModelViewSet)
# from app.views import MessageAPIView

urlpatterns = [
    path('',include(router.urls)),
    # path('message/',MessageAPIView.as_view(),name='message')
]