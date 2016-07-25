from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'^$', 'untitled.views.home', name='home'),
    url(r'^$', 'blog.views.home', name='bloghome'),
    url(r'^about$', 'blog.views.about', name='blogabout'),
    url(r'^blog/$', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
