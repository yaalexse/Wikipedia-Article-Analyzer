from django.urls import path,re_path
from . import views
from .views import get_data

urlpatterns = [
    path("<slug:title>", get_data, name = 'detail',)
    #    path('search/', views.search, name='search'),
]
