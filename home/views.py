from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("This is home page")
def login_view(request):
    return HttpResponse("This is login Page")
def signup_company_view(request):
    return HttpResponse("This is Company Singnup page")
def signup_passenger_view(request):
    return HttpResponse("This is Passenger Singnup page")
def faq_view(request):
    return HttpResponse("This is Faq Page")
def contact_us_view(request):
    return HttpResponse("This is contact us page")
def about_us_view(request):
    return HttpResponse("This is About us page")
