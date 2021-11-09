from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.search_questions,name='search'),
    path('back',views.back,name='back')
]