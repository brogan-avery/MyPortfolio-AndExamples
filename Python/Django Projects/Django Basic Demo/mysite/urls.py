from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url


urlpatterns = [
    path('to_do/', include('to_do.urls')),
    path('graph/', include('graph.urls')),
    path('helloworld/', include('helloworld.urls')),
    path('admin/', admin.site.urls),
]
