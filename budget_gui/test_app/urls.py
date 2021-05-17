from django.conf.urls import url
from test_app import views

# Template Tagging
app_name = 'test_app'

urlpatterns=[
    url(r'^$',views.index,name='index'),
	url(r'^relative/$',views.relative,name='relative'),
	url(r'^other/$',views.other,name='other'),
]
