from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.urls import path

urlpattern = [
    path('login', views.signUp),
    path('api-jwt=auth', obtain_jwt_token),
    path('api-jwt=auth', refresh_jwt_token),
    path('api-jwt=auth', verify_jwt_token)

]