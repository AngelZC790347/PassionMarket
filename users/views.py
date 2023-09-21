from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from  rest_framework.response import Response
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('birthday')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['POST','PUT'])
def manageUserPassword(request):
    return Response("changed")