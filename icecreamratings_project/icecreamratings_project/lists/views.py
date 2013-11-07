from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django.http import HttpRequest
from django.http import HttpResponse

from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    items = Item.objects.all().filter(list=list_.id)
    if request.method == 'POST':
        try:
            Item.objects.create(text=request.POST['item_text'], list=list_)
            return redirect(list_)

        except ValidationError:
            error = "You can't have an empty list item"
    return render(request, 'list.html', {'list': list_, 'error': error, 'items': items})


def new_list(request):
    list_ = List.objects.create()
    try:
        Item.objects.create(text=request.POST['item_text'], list=list_)
    except ValidationError:
        error_text = escape("You can't have an empty list item")
        return render(request, 'home.html', {"error": error_text})
    return redirect(list_)
