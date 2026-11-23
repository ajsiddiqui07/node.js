from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request,"jobindex.html")


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from .models import Job
from .serializers import JobSerializer

from jobPortal.permissions import IsRecruiter
from recruiters.models import RecruiterProfile


# =========================================================
# 1. Recruiter Job ViewSet
# =========================================================

class RecruiterJobViewSet(viewsets.ModelViewSet):

    serializer_class = JobSerializer
    permission_classes = [IsRecruiter]

    # -----------------------------------------------------
    # GET -> Recruiter ki sirf apni jobs
    # POST -> New job create
    # -----------------------------------------------------

    def get_queryset(self):

        return Job.objects.filter(
            posted_by=self.request.user
        ).order_by('-created_at')

    # -----------------------------------------------------
    # CREATE JOB
    # -----------------------------------------------------

    def perform_create(self, serializer):

        try:

            recruiter_profile = self.request.user.recruiter_profile

            company = recruiter_profile.company

            serializer.save(
                posted_by=self.request.user,
                company=company
            )

        except RecruiterProfile.DoesNotExist:

            raise ValidationError({
                "detail": "Recruiter profile is not configured correctly."
            })


# =========================================================
# 2. Public / Candidate Job ViewSet
# =========================================================

class PublicJobViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    # -----------------------------------------------------
    # GET -> Active jobs
    # -----------------------------------------------------

    def get_queryset(self):

        queryset = Job.objects.filter(
            is_active=True
        ).order_by('-created_at')

        # Search by title
        title = self.request.query_params.get('title')

        if title:

            queryset = queryset.filter(
                title__icontains=title
            )

        return queryset