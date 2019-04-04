from django.conf.urls import url
from pages import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_post/$', views.add_post, name='add_post'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/$', views.restricted, name='restricted'),
]
