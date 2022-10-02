from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage_admin_view(request):
    return HttpResponse("This is Admin Homepage")
