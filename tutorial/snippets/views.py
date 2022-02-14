from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

"""
List all code snippets, or create a new snippet.
"""
class SnippetList(generics.ListCreateAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer

"""
Retrieve, update, or delete a code snippet.
"""
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer