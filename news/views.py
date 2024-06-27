from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from . models import News


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trending'] =News.objects.all().order_by('-pub_date')[:3]
        context['rightcontent'] =News.objects.all().order_by('-pub_date')[3:5]
        return context


# class HomePageView(View):
#     def get(self,request):
#         return render(request, 'index.html')

class CategoryPageView(TemplateView):
    template_name = 'category.html'

class AboutUsPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class LatestNewsPageView(TemplateView):
    template_name = 'latest_news.html'