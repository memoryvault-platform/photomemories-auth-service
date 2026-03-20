from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def test_api(request):
    return Response({"message": "Auth Service is working"})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"})
    return Response(serializer.errors)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        user = User.objects.get(username=username)

        if user.password == password:
            return Response({"message": "Login successful"})
        else:
            return Response({"error": "Invalid password"})

    except User.DoesNotExist:
        return Response({"error": "User not found"})