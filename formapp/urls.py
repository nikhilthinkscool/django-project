from django.conf.urls import url


import views

app_name = 'formapp'
urlpatterns = [
        url('^$',views.index, name = "index"),
        url('^signup/$', views.signup, name = "signup"),
        url('^login/$', views.login, name = "login"),
        url('^update/$', views.update, name = "update"),
        url('^forgot/$', views.forgot, name = "forgot password"),
        url('^search/$', views.search, name = "search"),

]
