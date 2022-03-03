from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from accounts.models import CustomUser
from .serializers import (
    RegisterCustomUserSerializer, ChangePasswordSerializer, 
    UpdateUserSerializer)


class SignUpAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterCustomUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(data=serializer.data, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = UpdateUserSerializer



class BlackListTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class ChangePasswordAPIView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({"old_password": ["Neispravna lozinka."]}, 
                                status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success", 
                "code": status.HTTP_200_OK,
                "message": "Lozinka promijenjena!",
                "data": []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



