from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('edit-profile', views.edit_profile, name='edit-profile'),
    path('show-profile', views.show_profile, name='show-profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
