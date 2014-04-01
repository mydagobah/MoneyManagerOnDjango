from django.conf.urls import patterns, url

from MoneyManager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^getMDataByCategory/$', views.getMDataByCategory, name='mjson'),
    url(r'^getYDataByCategory/$' , views.getYDataByCategory, name='yjson'),
    url(r'^getDataByMonth/$', views.getDataByMonth, name='mjson'),
    url(r'^getDataByYear/$',  views.getDataByYear, name='yjson'),
    url(r'^getCategoryData/$',  views.getCategoryData, name='cmjson'),
)
