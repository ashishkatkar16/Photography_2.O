from django.urls import path

from . import views

urlpatterns = [
    # ------------------------ ADMIN URLS ------------------------
    path("", views.admin_index, name='admin_index'),
    path("admin_home", views.admin_home, name='admin_home'),
    path("admin_signup", views.admin_signup, name='admin_signup'),
    path("admin_dashboard", views.admin_dashboard, name='admin_dashboard'),
    # ------------------------ ADMIN END ------------------------

    # ------------------------ ADMIN URLS ------------------------
    path("user_index", views.user_index, name='user_index'),
    path("user_otp", views.user_otp, name='user_otp'),
    path("user_selfie", views.user_selfie, name='user_selfie'),
    path("user_dashboard", views.user_dashboard, name='user_dashboard'),
    # ------------------------ ADMIN URLS ------------------------
]
