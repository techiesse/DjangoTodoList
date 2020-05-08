from django.shortcuts import render, redirect

# Create your views here.
from .models import *

def checklist_list(request):
    checklists = Checklist.objects.all()
    context = {
        "checklists": checklists
    }
    return render(request, "Checklist/checklist_list.html", context)


def checklist_create(request):
    if request.method == "POST":
        name = request.POST.get("checklist_name")
        checklist = Checklist.objects.create(name = name)
        return redirect("checklist_list")
    return render(request, "Checklist/checklist_create.html")


def checklist_detail(request, id):
    checklist = Checklist.objects.get(id=id)
    items = checklist.item_set.all()

    context = {
        "checklist": checklist,
        "items": items,
    }
    return render(request, "Checklist/checklist_detail.html", context)
