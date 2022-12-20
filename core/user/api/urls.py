from django.urls import path, include
from .views import CustomLoginView, LoginInformationGenericView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'login-logs', LoginInformationGenericView, basename='login-logs')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomLoginView.as_view() ,name='login'),
]
