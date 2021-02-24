from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response,name):
    ls=ToDoList.objects.get(name=name)
    #Using a custom form here
    if response.method=="POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id))=="clicked": #if the checked response equals to the item id
                    item.complete=True
                else:
                    item.complete=False
        
        elif response.POST.get("newItem"):
            txt=response.POST.get("new")

            if len(txt)>2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid Input")
    

    return render(response, "main/list.html",{"ls":ls}) #dictionary is used to pass variables to the html

def home(response):
    return render(response, "main/home.html",{"name":'test name'})

def create(response):
    #response.user
    if response.method=="POST":
        form=CreateNewList(response.POST) #this is a dict

        if form.is_valid():
            n=form.cleaned_data['name'] 
            t=ToDoList(name=n) #creates a new todolist with the given name
            t.save()
            return HttpResponseRedirect("/%s" %t.name)

    else:    
        form=CreateNewList()
    
    return render(response, "main/create.html",{"form":form})

