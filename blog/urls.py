from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^archives.html$', views.archives, name='archives'),
    url(r'^category.html$', views.category, name='category')
]
