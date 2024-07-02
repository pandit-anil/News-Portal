from django.shortcuts import render
from rest_framework.generics import ListAPIView
from news.models import Category,News
from .serializers import CategorySerializer,NewsSerializer

class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsViews(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


