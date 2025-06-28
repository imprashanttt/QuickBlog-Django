"""
URL configuration for _02_blog_post project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from _02_blog_post import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("blog<id>/", views.blog_page, name="blog_page"),
    path("login/", views.login_user, name="loginUser"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("filter/", views.filter, name="filter"),
    path("search/", views.search, name="search"),
    path("donation/", views.donation, name="donation"),
    path("paymentQRGenerator/", views.paymentQr, name="payment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
