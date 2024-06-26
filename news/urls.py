from django.urls import path
from newsportal import settings
from django.conf.urls.static import static
from .views import AboutUsPageView, ContactPageView, LatestNewsPageView, CategoryPageView

urlpatterns = [
    path('about', AboutUsPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('latest', LatestNewsPageView.as_view(), name='latest_news'),
    path('category', CategoryPageView.as_view(), name='category'),
]