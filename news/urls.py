from django.urls import path
from newsportal import settings
from django.conf.urls.static import static
from .views import TeamViews, LatestNewsPageView, CategoryPageView
from . import views

urlpatterns = [
    path('about', TeamViews.as_view(), name='about'),
    path('contact', views.Contact, name='contact'),
    path('latest-news/<int:pk>/', LatestNewsPageView.as_view(), name='details'),
    path('category', CategoryPageView.as_view(), name='category'),
    path('comment/<int:id>/',views.Comments,name="comment"),
    
]