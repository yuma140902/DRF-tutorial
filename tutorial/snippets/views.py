from rest_framework import mixins
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

"""
List all code snippets, or create a new snippet.
"""
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

"""
Retrieve, update, or delete a code snippet.
"""
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)
  
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(self, request, *args, **kwargs)