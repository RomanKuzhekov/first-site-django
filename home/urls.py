from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^company/$', views.company, name='company'),
    url(r'^contacts/$', views.company, name='contacts'),
    url(r'^building/$', views.company, name='building'),
    url(r'^sale/$', views.company, name='sale'),
    url(r'^articles/$', views.articles_list, name='articles_list'),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.articles_detail, name='articles_detail'),
    url(r'^guestbook/$', views.guestbook, name='guestbook'),
    url(r'^guestbook_thanks/$', views.guestbook_thanks, name='guestbook_thanks'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^photos/$', views.photos, name='photos'),
]
