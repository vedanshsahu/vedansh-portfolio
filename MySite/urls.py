from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from MySite import settings
from feed import urls as feed_urls

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),  # admin site
    path('', include(feed_urls, namespace='feed')),
    path('tinymce/', include('tinymce.urls')),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
