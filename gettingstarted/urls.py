from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^live-map', hello.views.live_map, name='live_map'),
    url(r'^live-stream', hello.views.live_stream, name='live_stream'),
    url(r'^live-news', hello.views.live_news_links, name='live_news_links'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
