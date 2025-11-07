from django.urls import path
from . import views
urlpatterns = [
    path("new/",views.create_monster,name="create-monster"),
    path("",views.monster_list,name="monster-list"),
    path("<int:pk>/edit/",views.monster_update,name="update-monster"),
    #make a url for deleting monsters:
    path("<int:pk>/delete/",views.delete_monster,name="delete-monster")
]