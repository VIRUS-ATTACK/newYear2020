from django.urls import path

from . import views
urlpatterns = [
    path('newyear/<username>/',views.index,name = 'index'),
]