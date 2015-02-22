from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

# Included App URL Patterns
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('dream_bridge.apps.users.urls', namespace='users'))
)

# Main URL Patterns
urlpatterns += patterns('',
    url(r'^$', 'dream_bridge.views.home', name='home'),
    url(r'^login/', 'dream_bridge.views.login', name='login'),
    url(r'^sign-up/', 'dream_bridge.views.sign_up', name='sign_up'),
)

# Development
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = media + staticfiles_urlpatterns() + urlpatterns
