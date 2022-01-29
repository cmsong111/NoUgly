from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer

User = get_user_model()




JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email


    username = None
    name = serializers.CharField(max_length=15)
    date = serializers.DateField()
    gender = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=250)
    phone_num = serializers.CharField(max_length=16)



class UserLoginSerializer(LoginSerializer):
    # email = serializers.EmailField( max_length=255)
    # password = serializers.CharField(max_length=128, write_only=True)
    # token = serializers.CharField(max_length=255, read_only=True)
    
    
    
    # def validate(self, data):
    #     email = data.get("email", None)
    #     password = data.get("password", None)
    #     user = authenticate(email=email, password=password)

    #     if user is None:
    #         return {
    #             'id': 'None', 'email': email
    #         }
    #     try:
    #         payload = JWT_PAYLOAD_HANDLER(user)
    #         jwt_token = JWT_ENCODE_HANDLER(payload)
    #         update_last_login(None, user)
    #     except:
    #         raise serializers.ValidationError(
    #             'User with given email and password does not exists'
    #         )
    #     return {
    #         'id': user.id,
    #         'token': jwt_token
    #     }
     # 기본 설정 필드: username, password, email
    username = None
        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name','date', 'gender','address', 'phone_num')