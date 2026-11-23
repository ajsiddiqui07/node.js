from django.urls import path
from .views import *


urlpatterns = [
    path("index",index,name='index')
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CompanyProfileViewSet


router = DefaultRouter()

router.register(
    'company',
    CompanyProfileViewSet,
    basename='company'
)


urlpatterns = [
    path('', include(router.urls)),
]