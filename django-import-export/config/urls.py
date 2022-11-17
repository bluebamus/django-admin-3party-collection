#urls.py
from django.contrib import admin
from django.urls import path
from app.views import export

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.index),
    path('export-exl/', export, name='export'),
    path('export-csv/', export, name='export'),
]