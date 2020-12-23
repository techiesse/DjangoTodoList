from django.urls import path

from Checklist import api

from .views import *

urlpatterns = [
    path('create', checklist_create, name="checklist_create"),
    path('<int:id>/detail', checklist_detail, name="checklist_detail"),
    path('<int:id>/edit', checklist_edit, name="checklist_edit"),
    path('<int:id>/delete', checklist_delete, name="checklist_delete"),
    path('<int:id>/item_add', checklist_item_add, name="checklist_item_add"),
    path('<int:checklist_id>/item/<int:item_id>/check', api.check_item, name="api_checklist_item_check"),
    path('<int:checklist_id>/item_remove/<int:item_id>', checklist_item_remove, name="checklist_item_remove"),
    path('', checklist_list, name="checklist_list"),
]
