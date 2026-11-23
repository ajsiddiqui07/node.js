from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    index,
    SkillViewSet,
    CandidateProfileViewSet,
    ResumeViewSet,
    ProjectViewSet
)


router = DefaultRouter()


# Skills
router.register(
    'skills',
    SkillViewSet,
    basename='skills'
)


# Candidate Profile
router.register(
    'profile',
    CandidateProfileViewSet,
    basename='candidate-profile'
)


# Resume
router.register(
    'resume',
    ResumeViewSet,
    basename='resume'
)


# Projects
router.register(
    'projects',
    ProjectViewSet,
    basename='projects'
)


urlpatterns = [

    # Candidate Home
    path('index', index, name='candidate-index'),

    # Router
    path('', include(router.urls)),
]