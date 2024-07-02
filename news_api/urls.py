from django.urls import path,include
from . views import CategoryView,NewsViews
from . import views

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('category',CategoryView.as_view()),
    path('news',NewsViews.as_view()),

]
