from django.urls import path,include
from . views import CategoryView,NewsViews,NewsDeatil
from . import views

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('category',CategoryView.as_view({'get':'list'})),
    path('category/<int:pk>',CategoryView.as_view({'get':'retrive'})),
    path('news',NewsViews.as_view({'get':'list'})),
    path('news/<int:pk>', NewsViews.as_view({'get':'retrive'})),


]
