# defines URL patterns for learninig_logs

from django.conf.urls import urls

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name = 'index'),
]
