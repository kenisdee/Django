from django.urls import path
from . import views

urlpatterns = [
    path('class-based/', views.class_based_view, name='class_based_view'),
    path('function-based/', views.function_based_view, name='function_based_view'),
]