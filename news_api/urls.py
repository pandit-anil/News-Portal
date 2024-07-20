from django.urls import path,include
from . views import CategoryView,NewsViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('categories',CategoryView.as_view({'get':'list'})),
    path('categories/<int:pk>',CategoryView.as_view({'get':'retrieve'})),
    path('news',NewsViews.as_view({'get':'list'})),
    path('news/<int:pk>', NewsViews.as_view({'get':'retrieve'})),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
