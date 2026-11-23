from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import AuthViewSet, index



router = DefaultRouter()

router.register(
    'auth',
    AuthViewSet,
    basename='auth'
)


urlpatterns = [

    # Home
    path('', index, name='index'),

    # AuthViewSet
    path('', include(router.urls)),

    # JWT Refresh
    path(
        'auth/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]