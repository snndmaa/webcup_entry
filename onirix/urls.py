from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home', views.home, name='home'),
    path('form', views.dream_form, name='dream-form'),
    path('horoscope', views.horoscope, name='horoscope'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),
    path('loading', views.loading, name='loading'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
