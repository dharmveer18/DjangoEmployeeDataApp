
from django.contrib import admin
from django.urls import path, include
#from .views import MemberGenViewset, MemberList
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employee', MemberGenViewset, )

app_name = 'Employee/employee'
urlpatterns = [
    path('', include(router.urls)),
    path('list/', MemberList.as_view())
]
