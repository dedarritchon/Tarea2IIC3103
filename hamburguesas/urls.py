from django.conf.urls import url
from hamburguesas import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('hamburguesa', views.hamburguesa_list, name='hamburguesas'),
    path('hamburguesa/<pk>', views.hamburguesa_detail, name='hamburguesa'),
    path('ingrediente', views.ingrediente_list, name='ingredientes'),
    path('ingrediente/<pk>', views.ingrediente_detail, name='ingrediente'),
    path('hamburguesa/<h_pk>/ingrediente/<i_pk>', views.hamburguesa_edit, name='edit_hamburguer'),
]