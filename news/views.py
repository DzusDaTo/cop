from django.shortcuts import render
from django.views.generic import DetailView
from .models import Articles


def news_out(request):
    news_home = Articles.objects.order_by('-date')
    return render(request, 'news/news_out.html', {'news_home': news_home})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'



