from django.urls import path, re_path

from .views import BlogDetailView, BlogListView

urlpatterns = [
    path('footballnews/<uuid:pk>', BlogDetailView.as_view(), name='blog_detail'),
    re_path(r'^archive/$',
            BlogListView.as_view(
                template_name="blog/post_archive.html",
                page_template="blog/post_archive_page.html"),
            name="blog_archive"),
    # re_path(r'^latest/feed/$', LatestEntriesFeed()),
    re_path(r'^$', BlogListView.as_view(), name='blog_index'),
]
