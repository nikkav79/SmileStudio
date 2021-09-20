"""SmileStudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('mainpage.urls')),
    path('admin/', admin.site.urls),

    path('about/', include('about.urls')),
    path('lessons/', include('lessons.urls')),
    path('media/', include('media.urls')),
    path('news/', include('news.urls')),
    path('reviews/', include('reviews.urls')),
    path('team/', include('team.urls')),
    path('vacancy/', include('work.urls')),
    path('contacts/', include('contacts.urls')),
    path('rent/', include('rent.urls')),


    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api_service.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
