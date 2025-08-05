from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),  # ✅ Django 기본 admin 연결
]
