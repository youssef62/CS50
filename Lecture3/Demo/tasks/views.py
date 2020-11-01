from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect 
# Create your views here.


class newTaskForm (forms.Form) : 
    task = forms.CharField(label="New Task")
    

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render (request, "tasks/tasklist.html",{
        "tasks" : request.session["tasks"] 
    }) 


def add (request) : 
    if request.method == "POST" : 
        form = newTaskForm(request.POST)
        if form.is_valid() : 
            task = form.cleaned_data["task"]
            print(type(request.session["tasks"]))
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("task"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render ( request , "tasks/add.html" ,{
        "form" : newTaskForm()
    })
