"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from pages.views import home_view, contact_view, about_view, social_view
from recipe.views import recipe_detail_view, recipe_create_view, recipe_view, recipe_delete, recipe_edit
from user.views import user_login,register,user_logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',home_view,name='home'),
    path('recipe_create/',recipe_create_view),
    path('recipe_detail.html',recipe_detail_view),
    path('recipe_view.html/<id>/',recipe_view),
    path('recipe_delete/<id>/',recipe_delete),
    path('recipe_edit/<id>/',recipe_edit),
    path('login',user_login,name='login'),
    path('logout',user_logout,name='logout'),
    path('register',register),
    path('contact.html',contact_view),
    path('about.html',about_view),
    path('social/',social_view),
    path('admin/', admin.site.urls),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns +=staticfiles_urlpatterns()