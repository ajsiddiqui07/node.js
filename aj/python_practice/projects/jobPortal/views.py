from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import RegisterSerializer, UserSerializer
from .models import *


User = get_user_model()


def index(request):
    return render(request, "index.html")

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["email"] = user.email
        token["role"] = user.role

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data["user"] = UserSerializer(self.user).data

        return data


class AuthViewSet(viewsets.ViewSet):

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[AllowAny]
    )
    def register(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "message": "User registered successfully",
                    "user": UserSerializer(user).data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[AllowAny]
    )
    def login(self, request):

        serializer = CustomTokenObtainPairSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK
        )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsAuthenticated]
    )
    def user(self, request):

        if request.user.role == "admin":

            users = CustomUser.objects.all()

            serializer = UserSerializer(
                users,
                many=True
            )
            return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )

        if request.user.role == "candidate":
            serializer = UserSerializer(request.user)

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )