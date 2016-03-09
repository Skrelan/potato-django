from django.conf.urls import url
from django.contrib import admin

#from . import views
from .views import (
    posts_list,
    posts_create,
    posts_detail,
    posts_update,
    posts_delete,
	)
urlpatterns = [
    #url(r'^$', "posts.views.posts_list"), #the reason there is no xyz/ in xyz/$  is because this is the landing page. i.e index.html
    #url(r'^create/$', "posts.views.posts_create"),
    #url(r'^detail/$', "posts.views.posts_detail"),
    #url(r'^update/$', "posts.views.posts_update"),
    #url(r'^delete/$', "posts.views.posts_delete"),
	
	#url(r'^posts/$', "<appname>.views.<function_name>)",
   
    url(r'^$', posts_list, name="list"), #the reason there is no xyz/ in xyz/$  is because this is the landing page. i.e index.html
    url(r'^posts/create/$', posts_create),
    url(r'^(?P<id>\d+)/$', posts_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$', posts_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', posts_delete),
	#url(r'^posts/$', "<appname>.views.<function_name>)",



]
