from django.contrib import admin
from django.urls import path
from .views import get, getall, pub

urlpatterns = [
    path('<int:id>', get),
    path('', getall),
    path('pub', pub)
]
