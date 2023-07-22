#from django.shortcuts import render

from typing import Any, Dict
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from django.utils import timezone

# Create your views here.

class NewsList(ListView):
    queryset = Post.objects.order_by("-postDateTime")
    template_name = 'newspaper/news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['time_now'] = timezone.localtime(timezone.now())
        context['empty'] = None
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'newspaper/post.html'
    context_object_name = 'post'