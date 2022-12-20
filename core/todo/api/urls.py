from django.urls import path, include
from .views import TodoModelViewSet,RandomTodoAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo', TodoModelViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('random-todo/', RandomTodoAPIView.as_view(), name='random-todo'),
]
