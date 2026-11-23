from django.urls import path
from .views import *


urlpatterns = [
    path("index",index,name='index')
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    RecruiterJobViewSet,
    PublicJobViewSet
)


router = DefaultRouter()

router.register(
    'recruiter',
    RecruiterJobViewSet,
    basename='recruiter-jobs'
)

router.register(
    'public',
    PublicJobViewSet,
    basename='public-jobs'
)


urlpatterns = [
    path('', include(router.urls)),
]