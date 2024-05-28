
# import path function defines each route
from django.urls import path
from . import views

# holds each route we define for main_app
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('/finches', views.finches_index, name='index'),
]

