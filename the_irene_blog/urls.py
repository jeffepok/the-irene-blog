from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path

admin.autodiscover()
urlpatterns = [path('sitemap.xml', sitemap, {'sitemaps': {'cmspages':
    CMSSitemap}}), re_path(r'accounts/', include('accounts.urls')), path('', include('djangocms_blog.taggit_urls'))]
urlpatterns += i18n_patterns(path('admin/', admin.site.urls), path('',
    include('cms.urls')))
urlpatterns += []

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
        )
    urlpatterns += static(settings.STATIC_URL, document_root=settings.
        STATIC_ROOT)
