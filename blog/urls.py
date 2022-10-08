from django.urls import path

from .views import blog_list, BlogDetail, user_blog, blog_tags, detail_blog_author


urlpatterns = [
    path('', blog_list, name="home"),
    path('<str:slug>/', BlogDetail.as_view(), name='blog_detail'),
    path('blog/author/<str:author>/', user_blog, name='user_blog'),
    path('blog/tags/<str:tags>/', blog_tags, name="tags"),
    path('blog/author/<str:author>/blog/<str:slug>/', detail_blog_author, name="detail_blog_author")
]
