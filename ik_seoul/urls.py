"""
URL configuration for ik_seoul project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import include, path

from main import views as main_views


def root(request):
    hostname = request.get_host().partition(":")[0]
    if hostname == "dash.localhost":
        return redirect("dashboard:index")
    return main_views.index(request)


def favicon(request):
    return HttpResponse(status=204)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls")),
    path("favicon.ico", favicon, name="favicon"),
    path("", root, name="root"),
    path("", include("main.urls")),
]
