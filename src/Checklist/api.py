from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your apis here.
from .models import *
from .forms import *


def check_item(request, checklist_id, item_id):
    checklist = Checklist.objects.get(id = checklist_id)
    checked_state = request.POST.get('checked') == 'true'
    try:
        checklist.check_item(item_id, checked_state)
    except Exception as e:
        return JsonResponse({
            'status': 'fail',
            'message': str(e)
        })

    return JsonResponse({'status': 'ok'})
