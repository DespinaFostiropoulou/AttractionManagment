from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions, filters
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    Returns a list of all snippets
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('title','code','linenos','owner')
    search_fields = ['title','code']
    ordering_fields = ('title', 'owner')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('title', 'code', 'linenos', 'owner')
    search_fields = ['title', 'code']
    ordering_fields = ('title', 'owner')
