"""
URL configuration for eventures_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# eventures_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from eventures import urls as eventures_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(eventures_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]

# from django.contrib import admin
# from django.urls import path, include
# from eventures import urls as eventures_urls
# from rest_framework import routers
# from rest_framework import viewsets
# from eventures.views import StudentViewSet, OrganizationViewSet

# router = routers.DefaultRouter()
# router.register(r'students', StudentViewSet)
# router.register(r'organizations', OrganizationViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('admin/', admin.site.urls),
#     path('api/', include(eventures_urls)),
# ]
