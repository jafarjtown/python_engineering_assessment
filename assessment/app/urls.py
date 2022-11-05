
from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_parties),
    path('all/pollings/', views.all_polling_unit),
    path('lga_r/', views.lga_f),
    path('<str:p_u_i>/', views.polling_unit),
    path('<str:p_u_i>/edit', views.polling_unit_ed),
]