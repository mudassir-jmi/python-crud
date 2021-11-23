from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("add",views.add,name='add'),
    path('delete_item/<int:item_id>/', views.delete_item),
    path('edit_item/<int:item_id>/', views.edit_item),
]