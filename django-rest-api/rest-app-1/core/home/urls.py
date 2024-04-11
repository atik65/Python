from django.urls import path

from .views import home, home_delete, home_post, home_put

urlpatterns = [
    path("", home, name="home"),
    path("post/", home_post, name="home_post"),
    path("put/<id>/", home_put, name="home_put"),
    path("delete/<id>/", home_delete, name="home_delete"),
]
