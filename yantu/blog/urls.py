from django.conf.urls import  url
from blog import views

urlpatterns = (
                url(r'^$', views.add, name='add'),
                url(r'^showTitle',views.showTitle,name='mytitle')
                       )