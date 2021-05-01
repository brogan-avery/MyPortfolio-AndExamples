from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url


urlpatterns = [
    path('health/', include('health.urls')),
    path('diet/', include('diet.urls')),
    path('exercise/', include('exercise.urls')),
    path('admin/', admin.site.urls),
]
