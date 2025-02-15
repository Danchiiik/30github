from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from apps.users.serializers import ChangePasswordSerializer, ForgotPasswordFinishSerializer, ForgotPasswordSerializer, RegisterSerializer



User= get_user_model()



class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("You registered successfully. A link to activate your account has been sent to your email", status=status.HTTP_201_CREATED)
    

class ActivationApiView(APIView):
    def get(self, request, act_code):
        try:
            user = User.objects.get(act_code=act_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'message' : 'Success'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message' : 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)
        

class ChangePasswordApiView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context ={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response("Password is changed successfully", status=status.HTTP_200_OK)


class ForgotPasswordApiView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response("Code has been sent to your email", status=status.HTTP_200_OK)


class ForgotPasswordFinishApiView(APIView):
    def post(self, request):
        serializer = ForgotPasswordFinishSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Password updated succesfully', status=status.HTTP_200_OK) 


