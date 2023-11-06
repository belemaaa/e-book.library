from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from functools import reduce
from operator import __or
from django.db.models import Q
from . import serializers

class Member_signup(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = serializers.MemberSignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            validated_data = serializer.validated_data
            username = validated_data.get('username')
            email = validated_data.get('email')
            password = validated_data.get('password')
            phone_number = validated_data.get('phone_number')
            hashed_password = make_password(password)
            existing_user = models.Member.objects.filter(username=username)
            if existing_user:
                return Response({'status': 'request failed', 'error': 'user already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(password=hashed_password)
            return Response({'status': 'success', 'message': 'new user has been created.'}, status=status.HTTP_200_OK)
        return Response({'message': 'an error occurred.', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class Member_Login(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = serializers.MemberLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            validated_data = serializer.validated_data
            try:
                member = models.Member.objects.get(username=validated_data.get('username'))
            except models.Member.DoesNotExist:
                member = None
            if member is not None and check_password(validated_data.get('password'), member.password):
                token, created = Token.objects.get_or_create(user=member)
                return Response({
                    'status': 'success',
                    'access_token': token.key,
                    'user': {
                        'id': member.id,
                        'username': member.username,
                        'email': member.email,
                        'phone_number': member.phone_number
                    }
                }, status=status.HTTP_200_OK) 
            return Response({
                'status': 'Failed request', 'message': 'invalid credentals'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'an error occurred', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            