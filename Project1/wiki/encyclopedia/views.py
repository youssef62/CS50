from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import util
from markdown2 import Markdown
from django import forms 
from django.urls import reverse
from random import randrange

existing_error = "This page already exists ! "
non_existing_error = "The page you're searching for doesn't exist ! "

class entry_form(forms.Form) : 
    title = forms.CharField(widget=forms.Textarea,label="Entry Title :" , max_length=20) 
    content = forms.CharField(widget=forms.Textarea,label="Markdown :")


def index(request):

    entries = util.list_entries()
    entries = list(map(cap, entries))
    i = randrange(0, len(entries))
    entry = entries[i]
    
    if request.method == "POST" : 
        search_term = request.POST.get("search")
        return HttpResponseRedirect(reverse("index")+search_term)
    else :
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()        

        })

def cap(st) : 
    return st.capitalize()

def show_entry(request,entry): 
    markdowner = Markdown()
    entries = util.list_entries()
    entries = list(map(cap,entries))
    
    if entry.capitalize() in entries : 
        content = markdowner.convert(util.get_entry(entry))
        return render ( request , "encyclopedia/entry.html" , {
            "title" : entry ,
            "content" : content 
        })
    else : 
        request.session["message"] = non_existing_error
        return HttpResponseRedirect(reverse("error"))


def new_page(request) : 
    if request.method == "POST" : 
        form = entry_form(request.POST)
        if form.is_valid() : 
            title = form.cleaned_data["title"] 
            content = form.cleaned_data["content"]

            if title in util.list_entries() :
                request.session["message"] = existing_error
                return HttpResponseRedirect(reverse("error"))
            else :  
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse("index")+title) 
            
        else : 
            return render(request,"encyclopedia/new.html",{
                "form" : form 
            })
    else : 
        return render(request, "encyclopedia/new.html" , {
           "form" : entry_form() 
         })

def show_error(request) : 
    message = request.session["message"] 
    return render(request, "encyclopedia/error.html" , {
        "message" : message
    })


class edit_form(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="Markdown :")

def entry_to_form (entry) : 
    content = util.get_entry(entry)      
    data = {"content" : content }
    return edit_form(initial = data)


def edit(request,entry) : 
    if request.method == "POST" : 
        form = edit_form(request.POST)
        if form.is_valid() :
            content = form.data["content"]
            util.save_entry(entry,content)
            return HttpResponseRedirect(reverse("index")+entry)
        else :
            return render(request, "encyclopedia/edit.html", {
                "title": entry,
                "form": form
            })
    else :  
        return render(request, "encyclopedia/edit.html" , {
            "title" : entry , 
            "form" : entry_to_form(entry)
        })


def random_entry (request) : 
    entries = util.list_entries()
    entries = list(map(cap, entries))
    i = randrange(0, len(entries))
    entry = entries[i]
    return HttpResponseRedirect(reverse("index")+entry)
