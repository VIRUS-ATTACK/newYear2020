from django.urls import path

from . import views
urlpatterns = [
    path('newyear/<slug:username>/',views.index,name = 'index'),
]