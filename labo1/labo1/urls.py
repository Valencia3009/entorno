from django.contrib import admin
from django.urls import path
from bd.views import Lista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Lista),
   
]
