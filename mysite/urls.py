from django.conf.urls import include, url
import django.contrib.auth.views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('home.urls')),
]
# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns() + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
# )
