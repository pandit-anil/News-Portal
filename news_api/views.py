from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from news.models import Category,News
from .serializers import CategorySerializer,NewsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . filters import NewsFilter

class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsViews(ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_class = NewsFilter
    filterset_fields = ['category__name','title']
    search_fields = ['category__name','title']
    ordering_fields = ['category__name','views']

class NewsDeatil(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    



