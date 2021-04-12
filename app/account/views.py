# Create your views here.
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken

from account.serializer import UserSerializer
from rest_framework_jwt.settings import api_settings
import datetime

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class LoginView(ObtainJSONWebToken):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response_data['user'] = UserSerializer(user).data
            return Response(response_data)

        return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def register_view(request):
    s = UserSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    s.save()
    return Response(s.data)


@api_view(['GET'])
def current_user_view(request):
    return Response(UserSerializer(request.user).data)
