from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
		return RefreshToken.for_user(user)

	def validate(cls, attrs):
		data = super(TokenObtainPairSerializer, cls).validate(attrs)

		refresh = cls.get_token(cls.user)

		data['refresh'] = str(refresh)
		data['access'] = str(refresh.access_token)

		if cls.user.is_superuser:
			data['user_type'] = "super user"
		else:
			data['user_type'] = "user"	

		return data


class UserTokenObtainPairView(TokenObtainPairView):
	serializer_class = UserTokenObtainPairSerializer
	
		
		
