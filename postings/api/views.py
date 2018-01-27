from rest_framework import generics
from postings.models import BlogPost

class BlogPostRUDView(generics.RetrieveUpdateDestroyAPIView):
	pass
	lookup_field = 'pk'
	query_set = BlogPost.objects.all()

	def get_queryset(self):
		return BlogPost.objects.all()

	# def get_object(self):
	# 	pk = self.kwargs.get("pk")
	# 	return BlogPost.objects.get(pk=pk)