from django.shortcuts import render,HttpResponse

# Create your views here.
def passenger_view(request):
    return HttpResponse("This is Passenger page")
def sunlight_direction_view(request):
    return HttpResponse("This is Sunlight Direction page")
def term_and_condition_view(request):
    return HttpResponse("This is Term and Condition page")
def bus_tracking_view(request):
    return HttpResponse("This is Bus Tracking Page")
def bus_schedule_view(request):
    return HttpResponse("This is Bus Schedule Page")
def bus_reservation_view(request):
    return HttpResponse("This is Bus Reservation page")
def passenger_profile_view(request):
    return HttpResponse("This is Passenger Profile Page")
def purchase_ticket_view(request):
    return HttpResponse("This is Ticket Purchase page")
def payment_view(request):
    return HttpResponse("This is payment page")

