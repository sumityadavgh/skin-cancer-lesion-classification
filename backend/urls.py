from django.contrib import admin
from django.urls import path
from prediction.views import predict,home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/predict/', predict, name='predict'),
]