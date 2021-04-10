from django.contrib import admin
from django.urls import path
from user.views import logup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logup/', logup)
]
