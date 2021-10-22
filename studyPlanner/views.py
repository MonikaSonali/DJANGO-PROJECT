from django.shortcuts import render, redirect
from django.http import HttpResponse, request
import pandas as pd
from django.forms import ModelForm
# from .models import Post

# class PostForm(ModelForm):
#     class meta:
#         model = Post
#         fields = '__all__'
# Create your views here.


# def new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         form.save()
#         return redirect("/indexpage")
#     else:
#         form = PostForm()
#     return render(request, "sample.html", {"form": form})

def home(request):
    context = {'resourceItem': 'resourcesItems'}
    return render(request, 'homepage.html')
    # return render(request, 'homepage.html', {"context":context})





#
# def index(request):
#     # return HttpResponse(" Hy there Welcome ! ")
#      return render(request, "homepage.html")
#
# def sample(request):
#     # return HttpResponse("This is sample page")
#     return render(request, "sample.html")
#
# def pages(request, page):
#     text = ""
#     if page == "indexpage":
#         text = "This is the index page"
#         template = "homepage.html"
#     elif page == "sample":
#         text = "This is the sample page"
#         template = "sample.html"
#     # return HttpResponse(text)
#     return render(request, template)

def display(request):
    # import pdb
    # pdb.set_trace()

    # {'csrfmiddlewaretoken': ['mbZgV6jeTq9SF9xFkkokZiqLZxiil4xuvL5yffHQQ8SeyY0JrCUvPXRD6YQ0BS6H'],
    #  'lpnumber': ['KA51G5250'], 'fncName': ['cases']}
    lpnumber=request.POST['lpnumber']
    fncName = request.POST['fncName']
    context = {"lp": lpnumber, "fncName": fncName}
    return render(request, 'sample.html', {"lp": lpnumber, "fncName": fncName})

