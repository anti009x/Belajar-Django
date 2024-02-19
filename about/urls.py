# from django.contrib import admin
from django.urls import path

# from about import views
# from blog import views as Blog
# from contact import views as Kontak
# from autentikasi import views as LoginViews
from autentikasi import views as LogoutViews
urlpatterns = [
    # path ('dashboard/',views.index,name="index"),
    path ('dashboard/logout/',LogoutViews.logoutview,name="logout")
]