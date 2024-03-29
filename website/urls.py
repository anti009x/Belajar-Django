"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from about import views
from blog import views as Blog
from contact import views as Kontak
from autentikasi import views as LoginViews
from autentikasi import views as LogoutViews
from adminmodule import views as AdminViews



urlpatterns = [
    path('admin/', admin.site.urls),
    path ('adminview/',AdminViews.adminview,name="adminview"),
    path('insert-data/', AdminViews.insertData, name="insert_data"),
    path('update/<int:id>/', AdminViews.UpdateData),
    path('delete/<id>', AdminViews.DeleteData),

    path ('dashboard/',views.index,name="index"),
    path('blog/',Blog.blog,name="blog"),
    
    path ('kontak/',Kontak.kontak,name="kontak"),
    
    path ('',LoginViews.login_view,name="login"),
    
    path ('dashboard/logout/',LogoutViews.logoutview,name="logout")
    
    ]
