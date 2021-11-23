from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.utils import timezone
from todo.models import todo
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.


def index(request):
    items = todo.objects.all().order_by("-added_date")
    return render(request, "index.html", {
        'items': items
    })

@csrf_exempt
def add(request):
  if request.user.is_authenticated==True:
    added_date = timezone.now()
    text = request.POST['add_item']
    todo.objects.create(added_date=added_date, text=text)
    return HttpResponseRedirect("/")
  else:
    return redirect("login")
@csrf_exempt
def edit_item(reques,item_id):
    
    return HttpResponseRedirect("/")
    
@csrf_exempt
def delete_item(request, item_id):
    todo.objects.get(id=item_id).delete()
    return HttpResponseRedirect("/")