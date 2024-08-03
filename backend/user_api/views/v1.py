from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from user_api.serializers import UserSerializer

from user_api.models import User


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(f"Serializer Data: {serializer.data}")

            return Response({
                'message': 'User registered successfully',
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        credential = request.data.get('credential', None)
        password = request.data.get('password', None)

        if not credential:
            return Response({
                'errors': ['Log in credential missing.'],
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=credential)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=credential)
            except User.DoesNotExist:
                user = None

        if user is None:
            return Response({
                'errors': ['User not found.'],
            }, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({
                'errors': ['Invalid password'],
            }, status=status.HTTP_401_UNAUTHORIZED)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({
                'detail': 'Invalid credentials.'
                }, status=status.HTTP_401_UNAUTHORIZED)
