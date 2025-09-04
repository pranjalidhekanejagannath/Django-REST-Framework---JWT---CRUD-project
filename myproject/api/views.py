# from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, BookSerializer
from .models import Book
from .permissions import IsOwnerOrReadOnly
# Create your views here.


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
