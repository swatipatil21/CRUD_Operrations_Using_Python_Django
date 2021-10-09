"""CRUD_Operation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CRUD_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", student_view, name="student"),
    path("student_details_post", student_details_post_api_view, name="student_details_post"),
    path("student_list", student_list_view, name="student_list"),
    path("student_update/<int:id>", student_details_update, name="student_update"),
    path("student_patch_api/<int:pk>", student_patch_api_view, name="student_patch_api"),
    path("student_delete_api/<int:id>", student_delete_api_view, name="student_delete_api"),
]
