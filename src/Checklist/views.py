from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *


def checklist_list(request):
    checklists = Checklist.objects.all()
    context = {
        "checklists": checklists
    }
    return render(request, "Checklist/checklist_list.html", context)


def checklist_create(request):
    create_form = ChecklistForm(request.POST or None)
    if create_form.is_valid():
        name = create_form.cleaned_data["name"]
        checklist = Checklist.objects.create(name = name)
        return redirect("checklist_list")
    context = {
        "form": create_form,
    }
    return render(request, "Checklist/checklist_create.html", context)


def checklist_detail(request, id):
    checklist = Checklist.objects.get(id=id)
    items = checklist.item_set.all()

    context = {
        "checklist": checklist,
        "items": items,
    }
    return render(request, "Checklist/checklist_detail.html", context)


def checklist_edit(request, id):
    checklist = Checklist.objects.get(id=id)
    form = ChecklistForm(
        request.POST or None,
        instance=checklist
    )
    if form.is_valid():
        form.save()
        return redirect("checklist_list")

    context = {
        "form": form,
        "checklist": checklist,
    }
    return render(request, "Checklist/checklist_edit.html", context)


def checklist_delete(request, id):
    checklist = Checklist.objects.get(id=id)
    if request.method == 'POST':
        checklist.delete()
        return redirect("checklist_list")

    context = {
        'checklist': checklist
    }

    return render(request, 'Checklist/checklist_delete.html', context)
