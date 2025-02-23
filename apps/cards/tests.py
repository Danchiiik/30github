from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date
from rest_framework import status

from apps.cards.models import Cards
from apps.cards.serializers import CardsSerializer


User = get_user_model()


class CardsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='admin@gmail.com', password='12345678')

        self.user.is_active = True
        self.user.save()

        self.token = str(AccessToken.for_user(self.user))


        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.card = Cards.objects.create(
            owner=self.user,
            name="John",
            surname="Doe",
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
            country="USA",
            citizenship="American",
            gender="Male",
            city="New York",
            address="123 Main Street",
            phone="+123456789",
            email="johndoe@example.com",
            name_father="Robert",
            surname_father="Doe",
            name_mother="Jane",
            surname_mother="Doe",
            siblings=2,
            degree="Bachelor",
            previous_school="NY High School",
            status_of_studies="Finished",
            graduation=date(2023, 6, 1),
            study_country="USA",
            study_address="456 University Road",
            study_language="English",
            gpa=3.8,
            financial_support=True,
            essay="This is a test essay.",
            diploma=SimpleUploadedFile("diploma.pdf", b"file_content", content_type="application/pdf"),
            documents=SimpleUploadedFile("document.pdf", b"file_content", content_type="application/pdf"),
        )

    def test_serializer(self):
        card_data = {
            'owner': self.user.id,
            'name': 'John',
            'surname': 'Doe',
            'image': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
            'country': 'USA',
            'citizenship': 'American',
            'gender': 'male',
            'city': 'New York',
            'address': '123 Main Street',
            'phone': '+123456789',
            'email': 'johndoe@example.com',
            'name_father': 'Robert',
            'surname_father': 'Doe',
            'name_mother': 'Jane',
            'surname_mother': 'Doe',
            'siblings': 2,
            'degree': 'Bachelor',
            'previous_school': 'NY High School',
            'status_of_studies': 'Finished',
            'graduation': '2023-06-01',
            'study_country': 'USA',
            'study_address': '456 University Road',
            'study_language': 'English',
            'gpa': 3.8,
            'financial_support': True,
            'essay': 'This is a test essay.',
            'diploma': SimpleUploadedFile("diploma.pdf", b"file_content", content_type="application/pdf"),
            'documents': SimpleUploadedFile("document.pdf", b"file_content", content_type="application/pdf")
        }

        serializer = CardsSerializer(data=card_data)

        if serializer.is_valid():
            print(f"Validated data: {serializer.validated_data}")
            self.assertTrue(True)
        else:
            print(f"Serializer errors: {serializer.errors}")
            self.assertTrue(False)  


    def test_get_card_list(self):
        response = self.client.get('/api/v1/cards/')
        self.assertEqual(response.status_code, 200)

    def test_get_detail_card(self):
        response = self.client.get(f'/api/v1/cards/{self.card.id}/')
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_access(self):
        self.client.credentials()  
        response = self.client.get("/api/v1/cards/")
        self.assertEqual(response.status_code, 200)  

    def test_delete_card(self):
        response = self.client.delete(f'/api/v1/cards/{self.card.id}/')
        self.assertEqual(response.status_code, 204)

    def test_patch_card(self):
        updated_data = {'name': 'test'}

        response = self.client.patch(f'/api/v1/cards/{self.card.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)

        self.card.refresh_from_db()
        self.assertEqual(self.card.name, 'test')


    

        
