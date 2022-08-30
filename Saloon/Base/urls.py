from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'home_page'),
    path('about/',about, name='about_page'),
    path('gallery/',gallery, name='gallery_page'),
    path('style/<str:id>',style, name='style_page'),
]
