# eventures/views.py

from rest_framework import generics, permissions, status
from .models import Student, Organization
from .serializers import StudentSerializer, OrganizationSerializer, MyUserSerializer
from rest_framework.response import Response


# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = [permissions.IsAuthenticated]

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        user_data = self.request.data.get('user', {})
        student_data = self.request.data.get('student', {})

        # Create a new MyUser instance
        user_serializer = MyUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Associate the Student instance with the new MyUser instance
        student = Student.objects.create(
            user=user,
            first_name=student_data.get('first_name', ''),
            last_name=student_data.get('last_name', '')
        )

        return Response({
            'user': user_serializer.data,
            'student': StudentSerializer(student).data,
        }, status=status.HTTP_201_CREATED)



class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    permission_classes_by_action = {
        'create': [permissions.IsAdminUser],
        'list': [permissions.IsAuthenticated],
        'retrieve': [permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser],
        'partial_update': [permissions.IsAdminUser],
        'destroy': [permissions.IsAdminUser]
    }


# class OrganizationListCreateView(generics.ListCreateAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     permission_classes = [permissions.IsAuthenticated]

class OrganizationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]


# from django.contrib.auth import get_user_model
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_http_methods
# from rest_framework import generics, permissions, status, viewsets
# from rest_framework.response import Response
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import MyUser, Organization
# from .serializers import MyTokenObtainPairSerializer, MyUserSerializer, OrganizationSerializer


# User = get_user_model()


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
#     permission_classes = (permissions.AllowAny,)


# class MyUserCreateAPIView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = MyUserSerializer
#     permission_classes = (permissions.AllowAny,)


# class MyUserLoginAPIView(generics.GenericAPIView):
#     serializer_class = MyUserSerializer
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             return Response({'error': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)

#         if not user.check_password(password):
#             return Response({'error': 'Invalid email or password.'}, status=status.HTTP_400_BAD_REQUEST)

#         refresh = RefreshToken.for_user(user)

#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#             'user': MyUserSerializer(user).data
#         })


# class MyUserListAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = MyUserSerializer
#     authentication_classes = (JWTAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)


# class OrganizationViewSet(viewsets.ModelViewSet):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     permission_classes = [permissions.IsAuthenticated]


# @method_decorator(csrf_exempt, name='dispatch')
# @method_decorator(require_http_methods(["PUT"]), name='put')
# class ProfileView(LoginRequiredMixin, generics.View):
#     def get(self, request):
#         user_data = {
#             'email': request.user.email,
#             'first_name': request.user.first_name,
#             'last_name': request.user.last_name,
#             'city': request.user.city,
#             'phone': request.user.phone
#         }


# # from django.contrib.auth import get_user_model
# # from rest_framework import generics, permissions, status
# # from rest_framework_simplejwt.authentication import JWTAuthentication
# # from rest_framework_simplejwt.tokens import RefreshToken
# # from rest_framework.response import Response
# # from .serializers import *
# # from rest_framework_simplejwt.views import TokenObtainPairView
# # from rest_framework.permissions import AllowAny
# # from rest_framework.views import APIView
# # from rest_framework import generics
# # from django.shortcuts import get_object_or_404
# # from rest_framework.permissions import IsAuthenticated
# # from rest_framework import viewsets
# # from django.contrib.auth.mixins import LoginRequiredMixin
# # from django.views import View
# # from django.http import JsonResponse
# # from django.utils.decorators import method_decorator
# # from django.views.decorators.csrf import csrf_exempt
# # from django.views.decorators.http import require_http_methods
# # from .models import MyUser


# # class MyTokenObtainPairView(TokenObtainPairView):
# #     serializer_class = MyTokenObtainPairSerializer
# #     permission_classes = (AllowAny,)


# # User = get_user_model()


# # class MyUserCreateAPIView(generics.CreateAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = MyUserSerializer
# #     permission_classes = (AllowAny,)


# # class MyUserLoginAPIView(generics.GenericAPIView):
# #     serializer_class = MyUserSerializer
# #     authentication_classes = (JWTAuthentication,)
# #     permission_classes = (permissions.IsAuthenticated,)

# #     def post(self, request, *args, **kwargs):
# #         email = request.data.get('email')
# #         password = request.data.get('password')

# #         user = User.objects.filter(email=email).first()

# #         if user is None:
# #             return Response({'error': 'Invalid email or password.'}, status=400)

# #         if not user.check_password(password):
# #             return Response({'error': 'Invalid email or password.'}, status=400)

# #         refresh = RefreshToken.for_user(user)

# #         return Response({
# #             'refresh': str(refresh),
# #             'access': str(refresh.access_token),
# #             'user': MyUserSerializer(user).data
# #         })


# # class MyUserListAPIView(generics.ListAPIView):
# #     queryset = User.objects.all()
# #     serializer_class = MyUserSerializer
# #     authentication_classes = (JWTAuthentication,)
# #     permission_classes = (permissions.IsAuthenticated,)


# # class OrganizationViewSet(viewsets.ModelViewSet):
# #     queryset = Organization.objects.all()
# #     serializer_class = OrganizationSerializer
# #     permission_classes = [IsAuthenticated]


# # @method_decorator(csrf_exempt, name='dispatch')
# # class ProfileView(LoginRequiredMixin, View):
# #     def get(self, request):
# #         user_data = {
# #             'email': request.user.email,
# #             'first_name': request.user.first_name,
# #             'last_name': request.user.last_name,
# #             'city': request.user.city,
# #             'phone': request.user.phone,
# #             'allergies': request.user.allergies,
# #             'drinking_preferences': request.user.drinking_preferences,
# #         }
# #         return JsonResponse({'user_data': user_data})

# #     @method_decorator(require_http_methods(["PUT"]))
# #     def put(self, request):
# #         user = MyUser.objects.get(id=request.user.id)
# #         user.email = request.POST.get('email')
# #         user.first_name = request.POST.get('first_name')
# #         user.last_name = request.POST.get('last_name')
# #         user.city = request.POST.get('city')
# #         user.phone = request.POST.get('phone')
# #         user.allergies = request.POST.get('allergies')
# #         user.drinking_preferences = request.POST.get('drinking_preferences')
# #         user.save()
# #         return JsonResponse({'status': 'success'})


# # class StudentViewSet(viewsets.ModelViewSet):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer
# #     permission_classes = [IsAuthenticated]

# #     def list(self, request):
# #         queryset = self.get_queryset()
# #         serializer = self.get_serializer(queryset, many=True)
# #         return Response(serializer.data)

# #     def create(self, request):
# #         serializer = self.get_serializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data, status=status.HTTP_201_CREATED)

# #     def retrieve(self, request, pk=None):
# #         student = get_object_or_404(self.get_queryset(), pk=pk)
# #         serializer = self.get_serializer(student)
# #         return Response(serializer.data)

# #     def update(self, request, pk=None):
# #         student = get_object_or_404(self.get_queryset(), pk=pk)
# #         serializer = self.get_serializer(student, data=request.data, partial=True)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)

# #     def destroy(self, request, pk=None):
# #         student = get_object_or_404(self.get_queryset(), pk=pk)
# #         student.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
