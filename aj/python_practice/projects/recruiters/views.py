from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request,"recruindex.html")
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from jobPortal.permissions import IsRecruiter
from jobs.serializers import CompanySerializer


class CompanyProfileViewSet(viewsets.ViewSet):

    permission_classes = [IsRecruiter]

    # =====================================================
    # GET - Current Recruiter's Company
    # =====================================================

    @action(
        detail=False,
        methods=['get'],
        url_path='me'
    )
    def me(self, request):

        try:
            company = request.user.recruiter_profile.company

        except AttributeError:
            return Response(
                {
                    "detail": "Recruiter profile or company is not configured."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CompanySerializer(company)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # =====================================================
    # PUT/PATCH - Update Company
    # =====================================================

    @action(
        detail=False,
        methods=['put', 'patch'],
        url_path='update'
    )
    def update_company(self, request):

        try:
            company = request.user.recruiter_profile.company

        except AttributeError:
            return Response(
                {
                    "detail": "Recruiter profile or company is not configured."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CompanySerializer(
            company,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )