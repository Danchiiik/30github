from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.cards.views import CardsViewSet

from . import views


router = DefaultRouter()

router.register('', CardsViewSet)



urlpatterns = [
    path('api/v1/cards/', include(router.urls))
]

