from rest_framework import serializers
from datetime import datetime

from apps.cards.models import Cards, Documents


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = '__all__'


class CardsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    documents = DocumentSerializer(many=True, required=False)

    class Meta:
        model = Cards
        fields = '__all__'


    def create(self, validated_data):
        request = self.context.get('request')
        files_data = request.FILES.getlist('documents')  
        
        card = Cards.objects.create(**validated_data)

        for file in files_data:
            Documents.objects.create(card=card, document=file)

        return card
    

    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep['graduation'] = instance.graduation.strftime('%d.%m.%Y')
        return rep
    
