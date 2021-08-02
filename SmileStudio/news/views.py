from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsFlow
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin


class NewsDetails(ObjectDetailMixin, View):
    model = NewsFlow
    template = 'news/news_details.html'

# class NewsDetails(View):
#     def get(self, request, slug):
#         item = get_object_or_404(NewsFlow, slug__iexact=slug)
#         return render(request,
#                       template_name='news/news_details.html',
#                       context={'item': item
#                                })


def news(request):
    news = NewsFlow.objects.all()
    return render(request,
                  template_name='news/news.html',
                  context={'news': news
                           })

# def news_details(request, slug):
#     item = NewsFlow.objects.get(slug__iexact=slug)
#     return render(request,
#                   template_name='news/news_details.html',
#                   context={'item': item
#                            })