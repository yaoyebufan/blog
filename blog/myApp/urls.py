from django.urls import path,re_path
from .views import *
#必须加这句话py3
app_name="myApp"
urlpatterns = [
    re_path('^index/$', articlepage,name="articlepage"),
    re_path('^content/$', content,name="content"),
    re_path(r'^tocontent/(?P<id>\d+)$', tocontent,name="tocontent"),
    # re_path('^list/$', list1, name="list1"),
    re_path('^message/$', message,name="message"),
    re_path('^tomessage/$', tomessage,name="tomessage"),
    re_path('^tocomment/$', tocomment,name="tocomment"),
    re_path('^tocomment/(\d+)/$', comment1,name="comment"),
    re_path('^me/$', me,name="me"),
]