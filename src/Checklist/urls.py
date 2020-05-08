from django.urls import path

from .views import (
    checklist_create,
    checklist_delete,
    checklist_detail,
    checklist_edit,
    checklist_list,
)

urlpatterns = [
    path('create', checklist_create, name="checklist_create"),
    path('<id>/detail', checklist_detail, name="checklist_detail"),
    path('<id>/edit', checklist_edit, name="checklist_edit"),
    path('<id>/delete', checklist_delete, name="checklist_delete"),
    path('', checklist_list, name="checklist_list"),
]
