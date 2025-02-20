from rest_framework import serializers

from apps.cards.models import Cards


class CardsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Cards
        fields = '__all__'