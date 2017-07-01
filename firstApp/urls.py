from django.conf.urls import include,url
from firstApp import views

urlpatterns = [url(r'^$',views.index, name='home'),]

