from . import views
from django.urls import path

app_name = "food"

urlpatterns = [
    path('', views.index, name = "index"), 
    path("<int:item_id>/", views.detail, name = "detail"),
    path("add/", views.add_item, name = "add_item"),
    path('delete/<int:id>/', views.delete_item, name = "delete_item"),
]