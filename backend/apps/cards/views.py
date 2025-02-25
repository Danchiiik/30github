from django.shortcuts import render
from rest_framework.viewsets import mixins, GenericViewSet

from apps.cards.models import Cards
from apps.cards.permissions import CardsPermissions
from apps.cards.serializers import CardsSerializer



class CardsViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [CardsPermissions]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
