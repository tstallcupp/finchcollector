
# import path function defines each route
from django.urls import path
from . import views

# holds each route we define for main_app
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_twig/<int:twig_id>/', views.assoc_twig, name='assoc_twig'),
    path('twigs/', views.TwigList.as_view(), name='twigs_index'),
    path('twigs/<int:pk>/', views.TwigDetail.as_view, name='twigs_detail'),
    path('twigs/create/', views.TwigCreate.as_view(), name='twigs_create'),
]

