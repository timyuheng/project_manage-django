from django.conf.urls import url
from . import views

app_name = 'journal'
urlpatterns = [
    url(r'^$', views.user_login, name="user_login"),
    url(r'^add_journal/$', views.add_journal, name="add_journal"),
    url(r'^index/$', views.index, name="index"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^(?P<journal_id>[0-9]+)$', views.modify_journal, name="modify_journal")
]
