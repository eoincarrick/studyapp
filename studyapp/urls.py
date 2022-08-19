from django.contrib import admin
from django.urls import path, include

import base.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]

