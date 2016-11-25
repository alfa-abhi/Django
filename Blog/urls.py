from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^first.html$', views.index, name='index'),
    url(r'^contact.html/$',views.contact, name='contact'),
    url(r'^contact.html/message$',views.mess, name='mess'),
    url(r'^post.html/$',views.post, name="post"),
    url(r'^post.html/uploaded$',views.list, name="list"),
    url(r'^seppost.html$',views.seppost, name="sepost"),
    url(r'^logged$',views.login, name="login"),
    ]