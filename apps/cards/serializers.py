from rest_framework import serializers

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
        documents_data = validated_data.pop('documents', [])
        card = Cards.objects.create(**validated_data)
        
        for doc_data in documents_data:
            document = Documents.objects.create(file=doc_data['file'])
            card.documents.add(document)

        return card

    def update(self, instance, validated_data):
        documents_data = validated_data.pop('documents', None)

        if documents_data is not None:
            instance.documents.clear()
            for doc_data in documents_data:
                document = Documents.objects.create(file=doc_data['file'])
                instance.documents.add(document)

        return super().update(instance, validated_data)