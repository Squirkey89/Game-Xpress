from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_favourite, name='favourite'),
    path('add_to_favourite/<int:item_id>', views.add_to_favourite, name='add_to_favourite'),
    path('remove_favourite/<int:item_id>', views.remove_favourite, name='remove_favourite'),

]