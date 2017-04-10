from django.conf.urls import url
from . import views

urlpatterns = [
    # p
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    # ex: /blog/timofey/
    url(r'^timofey/$', views.PostListView.as_view(), name='timofey_post_list'), 
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share,name='post_share'),
]
