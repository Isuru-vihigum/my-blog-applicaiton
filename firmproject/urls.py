from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URL pattern for the Django admin interface
    path('admin/', admin.site.urls),

    # Include all URLs from the 'firmapp' app
    path('firmapp/', include('firmapp.urls')),
]
