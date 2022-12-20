from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import Todo
from .serializers import TodoSerializer

class TodoModelViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset
    

class RandomTodoAPIView(RetrieveAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = Todo.objects.filter(user=self.request.user).order_by('?').first()
        return obj