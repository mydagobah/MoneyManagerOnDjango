from django.conf.urls import patterns, url

from MoneyManager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^getMonthlyData/$', views.getMonthlyData, name='mjson'),
    url(r'^getYearlyData/$' , views.getYearlyData,  name='yjson'),
)
