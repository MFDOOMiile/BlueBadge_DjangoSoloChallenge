from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("p_list", views.p_list_view, name="p_list"),
    path("t_list", views.t_list_view, name="t_list"), 
    path("p_add", views.add_player, name="p_add"), 
    path("p_edit/<int:id>", views.p_edit, name="p_edit"),
    path("p_delete/<int:id>", views.p_delete, name="p_delete"),
    path("confirm_delete/<int:id>", views.confirm_delete, name="confirm_delete")
]