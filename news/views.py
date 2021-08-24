from django.shortcuts import render


def news_out(request):
    return render(request, 'news/news_out.html')
