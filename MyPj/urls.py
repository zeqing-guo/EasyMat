from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from pylab1.views import query, ajax, help

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'selab1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r"^$", query),
    url(r"^ajax/$", ajax),
    url(r"^help$", help)
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
