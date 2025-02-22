from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.cards.views import CardsViewSet


router = DefaultRouter()

router.register('', CardsViewSet)



urlpatterns = [
    path('', include(router.urls))
]

