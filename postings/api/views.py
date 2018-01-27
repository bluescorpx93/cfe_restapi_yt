from rest_framework import generics, mixins
from postings.models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	#query_set = BlogPost.objects.all()
	serializer_class = BlogPostSerializer

	def get_queryset(self):
		return BlogPost.objects.all()

	# def get_object(self):
	# 	pk = self.kwargs.get("pk")
	# 	return BlogPost.objects.get(pk=pk)

class BlogPostAPIView(mixins.CreateModelsMixin, generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = BlogPostSerializer

	def get_queryset(self):
		return BlogPost.objects.all()

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	# def put(self, request, *args, **kwargs):
	# 	return self.update(request, *args, **kwargs)

	# def patch(self, request, *args, **kwargs):
	# 	return self.update(request, *args, **kwargs)

