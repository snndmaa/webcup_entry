from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from onirix.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('onirix/', include('onirix.urls')),
    path('', home, name='home')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
