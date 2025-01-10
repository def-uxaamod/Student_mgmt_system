from django.contrib import admin
from django.urls import path
from mgmt_app import views

urlpatterns = [
    path("",views.home_page,name="home_page"),
    path("create/",views.entry_details,name="entry"),
    path("view/",views.see_details,name="view"),
    path("update/<int:id>/",views.update_details,name="update"),
    path("delete/<int:id>/",views.delete_details,name="delete"),
]