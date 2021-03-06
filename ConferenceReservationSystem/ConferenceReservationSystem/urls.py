"""ConferenceReservationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from JulaneHotel import views

app_name = 'JulaneHotel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.MyIndexView.as_view(),name="my_index_view"),
    path('reservation', views.MyReservationView.as_view(),name="my_reservation_view"),
    path('gallery', views.MyGalleryView.as_view(),name="my_gallery_view"),
    path('contact', views.MyContactView.as_view(),name="my_contact_view"),
    path('about', views.MyAboutView.as_view(),name="my_about_view"),
    path('LogIn', views.login,name="my_LogIn_view"),
    path('adminLogIn', views.MyadminLogInView,name="my_adminLogIn_view"),
    path('adminDashboard', views.MyadminDashboardView.as_view(),name="my_adminDashboard_view"),
    path('addRoom', views.MyaddRoomView.as_view(),name="my_addRoom_view"),
    path('customerRegistration', views.MyCustomerRegistration,name="my_customerRegistration_view"),
    path('dashboardCustomer', views.MydashboardCustomerView.as_view(),name="my_dashboardCustomer_view"),
    path('dashboardReservation', views.MydashboardReservationView.as_view(),name="my_dashboardReservation_view"),
    path('customerReservation', views.MyCustomerReservationView.as_view(),name="my_customerReservation_view"),
    path('customerDashboard', views.MyCustomerDashboardView.as_view(),name="my_customerDashboard_view"),
    path('customerProfile', views.MyCustomerProfileView.as_view(),name="my_customerProfile_view"),
    path('searchRoom', views.searchRoom,name="my_searchRoom_view"),
]
