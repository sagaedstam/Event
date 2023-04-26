# eventures/urls.py

from django.urls import path
from .views import (
    StudentListCreateView,
    StudentRetrieveUpdateDestroyView,
    OrganizationListCreateView,
    OrganizationRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),
    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', OrganizationRetrieveUpdateDestroyView.as_view(), name='organization-detail'),
]


# # eventures/urls.py
# from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from rest_framework import routers

# from .views import MyUserViewSet, StudentViewSet, OrganizationViewSet

# router = routers.DefaultRouter()
# router.register('users', MyUserViewSet)
# router.register('students', StudentViewSet)
# router.register('organizations', OrganizationViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
# ]
