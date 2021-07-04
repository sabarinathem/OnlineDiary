from django.urls import path
from diary import views
import diary


urlpatterns=[
    path('', views.index,name="index"),
    path('add/',views.add,name="add"),
    path('main/',views.main,name="main"),
    path('<int:id>/diary',views.diary,name="diary"),
    path('<int:id>/edit/',views.edit,name="edit")
]