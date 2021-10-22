from django.shortcuts import render, redirect
from django.http import HttpResponse, request
import pandas as pd

def home(request):
    # context = {'resourceItem': 'resourcesItems'}
    return render(request, 'homepage.html')
    # return render(request, 'homepage.html', {"context":context})

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
def casesHandled(request,licensePlate):
    Aresponse = "This is from cases function" + licensePlate
    return render(request, 'sample.html', {"A_res": Aresponse})

def getPublishInterval(request, license_plate):
    Bresponse = "This is from cases function" + license_plate
    return render(request, 'sample.html', {"B_res": Bresponse})


def display(request):
    import pdb
    pdb.set_trace()

    licensePlateNumber=request.POST['lpnumber']
    FunctionChosen = request.POST['fncName']


    print(licensePlateNumber,FunctionChosen)

    if licensePlateNumber and FunctionChosen == "cases":
        return redirect(casesHandled, licensePlate=licensePlateNumber)

    if licensePlateNumber and FunctionChosen == "pubInterval":
        return redirect(getPublishInterval, licensePlate=licensePlateNumber)


