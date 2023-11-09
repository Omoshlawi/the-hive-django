"""
URL configuration for the_hive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('properties/', include('properties.urls', namespace='properties')),
    path('blogs/', include('blog.urls', namespace='blogs')),
    path('sass/', include('sass.urls', namespace='sass')),
    path('agencies/', include('agencies.urls', namespace='agencies')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('', include('core.urls', namespace='core'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "The hive Admin"
admin.site.site_title = "The hive Admin"
