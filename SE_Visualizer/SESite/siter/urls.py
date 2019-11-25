from django.urls import path
from . import views

urlpatterns = [
    path("",views.inputPage,name="inputPage"),
    path("search/",views.searchResults,name="searchResults"),
]