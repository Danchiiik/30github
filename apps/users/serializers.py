from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.users.models import Profile
from apps.users.tasks import send_act_code_celery, send_confirmation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        if p1 != p2:
            raise serializers.ValidationError("Passwirds don't match")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        code = user.act_code
        send_act_code_celery.delay(user.email, code)
        user.save()
        return user
    


    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     user.set_password(validated_data['password'])
    #     code = user.activation_code
    #     send_act_code_celery.delay(user.email, code)
    #     user.save()
    #     return user
    

























    # password2 = serializers.CharField(min_length=8, required=True, write_only=True)
    
    # class Meta:
    #     model = User
    #     fields = ['email', 'password', 'password2']
         
    # def validate(self, attrs):
    #     p1 = attrs.get('password')
    #     p2 = attrs.pop('password2')
    #     if p1 != p2:
    #         raise serializers.ValidationError('Пароли не совпадают')
    #     return attrs
    
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     user.set_password(validated_data['password'])
    #     code = user.activation_code
    #     send_act_code_celery.delay(user.email, code)
    #     user.save()
    #     return user
    
