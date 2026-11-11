from django.urls import path
from . import views

urlpatterns = [
    path("box-recommendation/",views.box_recommendation,name="box_recommendation")
]
