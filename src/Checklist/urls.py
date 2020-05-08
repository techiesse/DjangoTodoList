from django.urls import path

from .views import (
    checklist_create,
    checklist_detail,
    checklist_list,
)

urlpatterns = [
    path('create', checklist_create, name="checklist_create"),
    path('detail/<id>', checklist_detail, name="checklist_detail"),
    path('', checklist_list, name="checklist_list"),
]
