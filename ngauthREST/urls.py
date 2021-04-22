from django.contrib import admin
from django.urls import path
from user.endpoints import UserViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewset)

urlpatterns = router.urls
urlpatterns += [ path('admin/', admin.site.urls) ]
