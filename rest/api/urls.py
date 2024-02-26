from django.urls import path
from api.views import StudentListView ,StudentretriveView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('student/', StudentListView.as_view() , name='student'),
    path('student/<int:pk>/', StudentretriveView.as_view() , name='students'),
    path('auth/login/', TokenObtainPairView.as_view() , name='create-Token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]