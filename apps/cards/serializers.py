from rest_framework import serializers

from apps.cards.models import Cards


class CardsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Cards
        fields = '__all__'