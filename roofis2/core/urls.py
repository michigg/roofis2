"""respool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from rest_framework.authentication import BasicAuthentication
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny

urlpatterns = [
    path('admin/', admin.site.urls),
    # APIs
    # path('api/', include('respool.api.urls')),

    # API Docs
    # path('api/docs/', include_docs_urls(title='Respool API Docs', public=True,
    #                                     authentication_classes=[BasicAuthentication, ],
    #                                     permission_classes=[AllowAny, ])),
]
