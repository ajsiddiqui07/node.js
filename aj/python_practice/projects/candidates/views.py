from django.shortcuts import render

from rest_framework import viewsets, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import CandidateProfile, Skill, Project

from .serializers import (
    CandidateProfileSerializer,
    SkillSerializer,
    ProjectSerializer,
    ResumeUploadSerializer
)

from jobPortal.permissions import IsCandidate


# =========================================================
# Candidate Home Page
# =========================================================

def index(request):
    return render(request, "canindex.html")


# =========================================================
# 1. SKILL VIEWSET
# =========================================================

class SkillViewSet(viewsets.ModelViewSet):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    # Only List + Create
    http_method_names = ['get', 'post']


# =========================================================
# 2. CANDIDATE PROFILE VIEWSET
# =========================================================

class CandidateProfileViewSet(viewsets.ViewSet):

    permission_classes = [IsCandidate]

    # -----------------------------------------
    # GET PROFILE
    # -----------------------------------------

    @action(
        detail=False,
        methods=['get'],
        url_path='userprofile'
    )
    def userprofile(self, request):

        profile, _ = CandidateProfile.objects.get_or_create(
            user=request.user
        )

        serializer = CandidateProfileSerializer(profile)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    # -----------------------------------------
    # UPDATE PROFILE
    # -----------------------------------------

    @action(
        detail=False,
        methods=['put', 'patch'],
        url_path='update'
    )
    def update_profile(self, request):

        profile, _ = CandidateProfile.objects.get_or_create(
            user=request.user
        )

        serializer = CandidateProfileSerializer(
            profile,
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


# =========================================================
# 3. RESUME VIEWSET
# =========================================================

class ResumeViewSet(viewsets.ViewSet):

    permission_classes = [IsCandidate]

    parser_classes = [
        parsers.MultiPartParser,
        parsers.FormParser
    ]

    # -----------------------------------------
    # UPLOAD RESUME
    # -----------------------------------------

    @action(
        detail=False,
        methods=['put', 'patch'],
        url_path='upload'
    )
    def upload(self, request):

        profile, _ = CandidateProfile.objects.get_or_create(
            user=request.user
        )

        serializer = ResumeUploadSerializer(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Resume uploaded successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# =========================================================
# 4. PROJECT VIEWSET
# =========================================================

class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsCandidate]

    # -----------------------------------------
    # ONLY CURRENT CANDIDATE PROJECTS
    # -----------------------------------------

    def get_queryset(self):

        return Project.objects.filter(
            candidate__user=self.request.user
        )

    # -----------------------------------------
    # CREATE PROJECT
    # -----------------------------------------

    def perform_create(self, serializer):

        profile, _ = CandidateProfile.objects.get_or_create(
            user=self.request.user
        )

        serializer.save(
            candidate=profile
        )

    # -----------------------------------------
    # OPTIONAL: MY PROJECTS
    # -----------------------------------------

    @action(
        detail=False,
        methods=['get'],
        url_path='my-projects'
    )
    def my_projects(self, request):

        projects = self.get_queryset()

        serializer = self.get_serializer(
            projects,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
