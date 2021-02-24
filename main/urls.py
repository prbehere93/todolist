from django.urls import path
from . import views #imports views from the current directory

urlpatterns = [
    path("<str:name>", views.index, name='index'),
    path("", views.home, name='home'),
    path("create/",views.create,name="create"),
    path("view/",views.view,name="view"),
    ]
