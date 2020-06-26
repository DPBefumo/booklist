from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, NoteSerializer, BookSerializer
from .models import User, Note, Book, get_available_books_for_user
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'author', 'title']

    def get_queryset(self):
        queryset = get_available_books_for_user(Book.objects.all(), self.request.user)

        return queryset

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
