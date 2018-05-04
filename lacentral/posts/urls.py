from django.conf.urls import url
from django.contrib import admin

from posts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^(?P<slug_post>[-\w\d]+)/$', views.post_view, name='post_view'),
]