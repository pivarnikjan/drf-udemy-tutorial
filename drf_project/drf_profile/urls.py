from django.conf.urls import url

from drf_profile import views

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
]

