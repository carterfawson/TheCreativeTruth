from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    #url(r'^$', 'blog.views.home', name='bloghome'),
    url(r'^post/(?P<question_id>[0-9]+)/$', 'blog.views.post', name='post')

]