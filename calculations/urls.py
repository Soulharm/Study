from django.contrib import admin
from django.urls import path

from calculations.views import *

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('mult/', multiplication, name='multiplication')
]
