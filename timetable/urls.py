from os import stat
from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = "index"),
    path('index3/',views.index1,name ="index1"),
    path('index2/',views.index2, name = "index2"),
]

