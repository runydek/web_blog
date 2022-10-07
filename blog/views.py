from django.views.generic import ListView, DetailView

from .models import Blog


class BlogList(ListView):
    queryset = Blog.objects.order_by('-created_on')
    model = Blog
    template_name = 'index.html'


class BlogDetail(DetailView):
    model = Blog
    template_name = 'detail.html'
