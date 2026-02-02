from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer, UserCreateSerializer, CustomTokenObtainPairSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsAdmin
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from .serializers import SignupSerializer
from rest_framework.permissions import IsAuthenticated



User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        """
        Only ADMIN can manage users.
        """
        if self.action in ["list", "create", "update", "partial_update", "destroy"]:
            return [IsAdmin(), IsAuthenticated()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        """
        Use different serializer for creation.
        """
        if self.action == "create":
            return UserCreateSerializer
        return UserSerializer

    @action(detail=False, methods=["get"], url_path="me", permission_classes=[IsAuthenticated],)
    def me(self, request):
        """
        Returns logged-in user's details.
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    
class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "message": "User registered successfully",
                "username": user.username,
            },
            status=status.HTTP_201_CREATED,
        )


