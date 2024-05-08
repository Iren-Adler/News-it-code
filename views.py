from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import models
#5.10
def index(request):
    news = models.News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список  новостей'})
