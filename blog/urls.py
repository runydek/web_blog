from django.urls import path

from .views import BlogList, BlogDetail


urlpatterns = [
    path('', BlogList.as_view(), name="home"),
    path('<str:slug>/', BlogDetail.as_view(), name='blog_detail')
]
