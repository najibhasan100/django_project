from django.shortcuts import render,HttpResponse

# Create your views here.

def home_company_view(request):
    return HttpResponse("This is our comapny home page")
def bus_registration_company_view(request):
    return HttpResponse("This is our comapny bus registration page")
def company_profile_view(request):
    return HttpResponse("This is Company profile Page")


