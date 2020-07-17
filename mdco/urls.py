from django.contrib import admin
from django.urls import path, include
from mdcore.views import index
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index)
]

