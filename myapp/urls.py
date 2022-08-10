from django.urls import path

from myapp import views

urlpatterns = [

path("", views.trans_view, name="trans_view")
]
