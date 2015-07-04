from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from test_storm import settings

urlpatterns = patterns('',
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^grappelli/', include('grappelli.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('website.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
