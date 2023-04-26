# eventures/urls.py
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', MyUserCreateAPIView.as_view(), name='user_create'),
    path('user/login/', MyUserLoginAPIView.as_view(), name='user_login'),
    path('user/list/', MyUserListAPIView.as_view(), name='user_list'),
    path('organization/', OrganizationViewSet.as_view({'get': 'list', 'post': 'create'}), name='organization'),
    path('organization/<int:pk>/', OrganizationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='organization_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
