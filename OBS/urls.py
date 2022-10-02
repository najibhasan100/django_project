"""OBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import home.views as home
import company.views as com
import passenger.views as pas
import homepage_admin.views as homadm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_company/', com.home_company_view),
    path('bus_registration_company/', com.bus_registration_company_view),
    path('about_us/', home.about_us_view),
    path('bus_reservation/', pas.bus_reservation_view),
    path('company_profile/', com.company_profile_view),
    path('company_profile/', com.company_profile_view),
    path('home/', home.home_view),
    path('passenger/', pas.passenger_view),
    path('contact_us/', home.contact_us_view),
    path('faq/', home.faq_view),
    path('homepage_admin/', homadm.homepage_admin_view),
    path('login/', home.login_view),
    path('bus_schedule/', pas.bus_schedule_view),
    path('bus_tracking/', pas.bus_tracking_view),
    path('passenger_profile/', pas.passenger_profile_view),
    path('payment/', pas.payment_view),
    path('purchase_ticket/', pas.purchase_ticket_view),
    path('signup_company/', home.signup_company_view),
    path('signup_passenger/', home.signup_passenger_view),
    path('sunlight_direction/', pas.sunlight_direction_view),
    path('term_and_condition/', pas.term_and_condition_view),

    ]
