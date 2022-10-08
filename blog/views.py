from django.shortcuts import render
from django.views.generic import DetailView

from .models import Blog, Tag, User


def blog_list(request):
    blogs = Blog.objects.all()
    tags = Tag.objects.all()

    context = {
        'blogs': blogs,
        'tags': tags
    }

    return render(request, 'index.html', context)


class BlogDetail(DetailView):
    model = Blog
    template_name = 'detail.html'


def user_blog(request, author):
    blog = Blog.objects.filter(author__username=author)

    context = {
        'blog': blog,
    }

    return render(request, 'blog_user.html', context)


def blog_tags(request, tags):
    blogs = Blog.objects.filter(tags__title=tags)

    context = {
        'blogs': blogs
    }

    return render(request, 'tag.html', context)


def detail_blog_author(request, author, slug):
    detail = Blog.objects.get(author__username=author, slug=slug)
    context = {
        'detail': detail
    }

    return render(request, 'detail_user_post.html', context)
