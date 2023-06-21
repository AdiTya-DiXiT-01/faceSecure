from django.contrib import admin
from django.urls import path
from .views import home, register, login, greeting
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('greeting/<int:face_id>/', greeting, name='greeting')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
