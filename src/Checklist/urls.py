from django.urls import path

from .views import (
    checklist_item_add,
    checklist_item_remove,
    checklist_create,
    checklist_delete,
    checklist_detail,
    checklist_edit,
    checklist_list,
)

urlpatterns = [
    path('create', checklist_create, name="checklist_create"),
    path('<int:id>/detail', checklist_detail, name="checklist_detail"),
    path('<int:id>/edit', checklist_edit, name="checklist_edit"),
    path('<int:id>/delete', checklist_delete, name="checklist_delete"),
    path('<int:id>/item_add', checklist_item_add, name="checklist_item_add"),
    path('<int:checklist_id>/item_remove/<int:item_id>', checklist_item_remove, name="checklist_item_remove"),
    path('', checklist_list, name="checklist_list"),
]
