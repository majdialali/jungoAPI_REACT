from django.urls import path
from .views import *  # Import your function-based view
# from django.contrib.auth.views import LoginView, LogoutView


from .views import RegisterAPIView, GetAllUsersAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

    

urlpatterns = [
    # path('', get_home),
    # path('home1/', get_home, name='home_msg'),  # http://127.0.0.1:8000/home/

    # path('home2/', home_view, name="home_html_pg"),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),


    path('api/register/', RegisterAPIView.as_view(),
         name='api-register'),  # ✅ New user registration API
    path('api/get_users/', GetAllUsersAPIView.as_view(),
         name='api-get-users'),  # ✅ New view for fetching users
    path("api/login/", LoginAPIView.as_view(), name="api-login"),
    path("api/get_user/", GetUserAPIView.as_view(), name="api-get-user"),
    path("api/get_user/", GetUserAPIView.as_view(), name="api-get-user"),

    # ✅ Login (get JWT) ..  built-in views not like custom function  we define in views.py
    #TokenObtainPairView → Handles user login and returns an access token and a refresh token.
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain"),
    
    # ✅ Refresh token .. built-in views not like custom lib
    #TokenRefreshView → Takes a refresh token and returns a new access token (without logging in again).
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

