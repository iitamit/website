from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("settings/", views.save_settings, name="save_settings"),
    path("stories/add/", views.add_story, name="add_story"),
    path("fashion/add/", views.add_fashion_look, name="add_fashion_look"),
    path("charts/add/", views.add_chart_entry, name="add_chart_entry"),
    path("videos/add/", views.add_video, name="add_video"),
    path("dramas/add/", views.add_drama, name="add_drama"),
    path("<str:model_name>/<int:pk>/delete/", views.delete_item, name="delete_item"),
]
