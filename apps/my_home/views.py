#from django.http import HttpResponse  # Import HttpResponse
#from .models import UserProfile

from rest_framework.response import Response

from rest_framework import status
#from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


""" related to traditional jungo forms

def get_home(request):
    return HttpResponse(f"Welcome to home page {request}")



def home_view(request):
    return render(request, 'home.html')  # Loads home.html

#call our db-table to get a user list


"""



"""

Receives user data (POST request) from the frontend.
Validates and saves the new user.
Returns a JSON response.

"""





User = get_user_model()  # ✅ Now using UserProfile instead of default User

class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        phone_number = request.data.get('phone_number')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password, phone_number=phone_number)
        return Response({"message": "User registered successfully", "user": {"username": user.username}}, status=status.HTTP_201_CREATED)




    

class GetAllUsersAPIView(APIView):
    """Returns all registered users"""
      
    def get(self, request):
        
        users = User.objects.all().values('id', 'username', 'email','phone_number')  # Get all users (ID, username, email)
        return Response({"get_users": list(users)}, status=status.HTTP_200_OK)

"""
to add a new user after running the server, open new poweshell and run: 
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/register/" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"username": "newuser", "email": "new@example.com", "password": "securepass123"}'

"""

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView
#from rest_framework.permissions import IsAuthenticated

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)  # ✅ Check user

        if user is not None:
            refresh = RefreshToken.for_user(user)  # ✅ Generate JWT token
           
            return JsonResponse({
                "access": str(refresh.access_token),  # ✅ Short-lived token (used for requests)
                "refresh": str(refresh)  # ✅ Long-lived token (used to get new access tokens)
            }, status=200)
        else:
            return JsonResponse({"error": "Invalid username or password"}, status=400)


from rest_framework.permissions import IsAuthenticated

class GetUserAPIView(APIView):
    permission_classes = [IsAuthenticated]  # ✅ Requires JWT authentication

    def get(self, request):
        if request.user.is_authenticated: 
            return JsonResponse({"username": request.user.username}, status=200)
        else:
            return JsonResponse({"error": "Unauthorized"}, status=401)


