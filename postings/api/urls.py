from .views import BlogPostRUDView, BlogPostAPIView
from django.conf.urls import url

urlpatterns = [
	url(r'^$', BlogPostAPIView.as_view(), name='post-listcreate'),
   url(r'^(?P<pk>\d+)/$', BlogPostRUDView.as_view(), name='post-rud'),
]
