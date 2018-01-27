from rest_framework import serializers
from postings.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogPost
		fields = [
			'pk', 'user', 'title', 'content', 'timestamp'
		]
		read_only_fields = ['pk', 'user']

	def validate_title(self, value):
		qs = BlogPost.objects.filter(title__iexact=value)
		if qs.exists:
			raise serializers.ValidationError("Title must be unique")
		return value 