from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet, base_name = 'users')

urlpatterns =[
    path('login/', TokenObtainPairView.as_view(), name = 'login'),
    path('login/refresh/', TokenRefreshView.as_view(), name = 'login_refresh'),
    path('', include(router.urls)),
]
