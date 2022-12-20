from rest_auth.views import LoginView
from ..models import LoginInformation
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from .serializers import LoginInformationSerializer
from rest_framework.viewsets import GenericViewSet

class LoginInformationGenericView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAdminUser]
    queryset = LoginInformation.objects.all()
    serializer_class = LoginInformationSerializer

class CustomLoginView(LoginView):
    def login_log(self, user, remote_addr=None, 
                  is_success=True, description=None
                  ):
         LoginInformation.objects.create(
             user=user, 
             is_success=is_success, 
             description=description, 
             remote_addr=remote_addr
            )

    def post(self, request, *args, **kwargs):
        try:
            result = super(CustomLoginView, self).post(request, *args, **kwargs)
            self.login_log(
                request.user, 
                is_success=True, 
                remote_addr=request.META.get('REMOTE_ADDR')
                )
            return result
        except Exception as e:
            username = request.data.get('username')
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                self.login_log(
                    user, 
                    is_success=False,
                    description=e.detail,
                    remote_addr=request.META.get('REMOTE_ADDR')
                    )
            raise e
        
        
