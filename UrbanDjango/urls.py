from django.contrib import admin
from django.urls import path, include
from task4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('tours/', views.page1_view, name='page1'),
    path('cart/', views.page2_view, name='page2'),
    path('task5/', include('task5.urls')),
]