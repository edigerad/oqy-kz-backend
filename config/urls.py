"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import ugettext_lazy as _
from rest_framework.documentation import include_docs_urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v0/', include('rest_auth.urls')),
                  path('api/v0/registration/', include('rest_auth.registration.urls')),
                  path('i18n/', include('django.conf.urls.i18n')),
                  path('api/docs/',
                       include_docs_urls(title='Oqy.kz API documentation',
                                         authentication_classes=[],
                                         permission_classes=[])),
              ] + static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)

admin.site.site_header = _("Oqy.kz Admin")
admin.site.site_title = _("Oqy.kz Admin Portal")
admin.site.index_title = _("Welcome to Oqy.kz Portal")
