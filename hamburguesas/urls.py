from django.conf.urls import url
from hamburguesas import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('hamburguesa/', views.hamburguesa_list, name='hamburguesas'),
    path('hamburguesa/<int:pk>/', views.hamburguesa_detail, name='hamburguesa'),
]