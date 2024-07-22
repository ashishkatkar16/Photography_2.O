from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path


urlpatterns = [
    # ------------------------ ADMIN URLS ------------------------
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("", views.admin_index, name='admin_index'),
    path("admin_home", views.admin_home, name='admin_home'),
    path("admin_home1/<int:customer_id>/", views.admin_home1, name='admin_home1'),
    path("user_images/<int:event_id>/", views.user_images, name='user_images'),
    path("admin_signup", views.admin_signup, name='admin_signup'),
    path("admin_dashboard", views.admin_dashboard, name='admin_dashboard'),
    # ------------------------ ADMIN END ------------------------

    # ------------------------ USER URLS ------------------------
    path("user_index", views.user_index, name='user_index'),
    path("user_otp", views.user_otp, name='user_otp'),
    path("user_selfie", views.user_selfie, name='user_selfie'),
    path("user_dashboard", views.user_dashboard, name='user_dashboard'),
    # ------------------------ USER URLS ------------------------

    # Logout
    path("logout", views.logout, name='logout'),
    # update user
    path('update_user/<int:id>', views.update_user, name='update_user'),
    # deleting user
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    # deleting events
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    # 404 page
    path('404', views.error_404, name='error_404'),
    # loader
    path('loader', views.loader_page, name='loader_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)