from django.urls import path

from .views import blog_list, BlogDetail, user_blog, blog_tags


urlpatterns = [
    path('', blog_list, name="home"),
    path('<str:slug>/', BlogDetail.as_view(), name='blog_detail'),
    path('blog/author/<slug:author>/', user_blog, name='user_blog'),
    path('blog/tags/<slug:tags>/', blog_tags, name="tags")
]
