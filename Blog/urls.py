from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path("" , views.index , name = "index"),      #default host url
    path("post/<int:post_id>", views.detail, name = "detail"),
    path("new_url", views.new_url_view, name="new_page_url"),
    path("old_url", views.old_url_redirect, name="old_url")
]