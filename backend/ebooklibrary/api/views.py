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

# Create your views here.
