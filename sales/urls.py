from django.urls import path
from . import views

urlpatterns = [
    path('nova/', views.create_sale, name='create_sale'),
]