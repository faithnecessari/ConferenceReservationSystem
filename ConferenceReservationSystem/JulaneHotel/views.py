from django.http import Http404
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
import mysql.connector
from django.contrib import messages
from .forms import *
from .models import *
from JulaneHotel.models import Rooms
from operator import itemgetter

# Create your views here.
class MyIndexView(View):
	def get(self, request):
		return render(request,'index.html', {})

class MyReservationView(View):
	def get(self, request):
		return render(request,'reservation.html', {})

class MyGalleryView(View):
	def get(self, request):
		return render(request,'gallery.html', {})

class MyContactView(View):
	def get(self, request):
		return render(request,'contact.html', {})

class MyAboutView(View):
	def get(self, request):
		return render(request,'about.html', {})

class MyLogInView(View):
	def get(self, request):
		return render(request,'LogIn.html', {})

class MyadminLogInView(View):
	def get(self, request):
		return render(request,'adminLogIn.html', {})

class MycustomerRegistrationView(View):
    def get(self, request):

        return render(request,'customerRegistration.html') 

    def post(self, request):
        form = CustomerForm(request.POST)

        if form.is_valid():
            firstname = request.POST.get("firstname")         
            lastname = request.POST.get("lastname")
            username = request.POST.get("username")
            password = request.POST.get("password")
            address = request.POST.get("address")
            contactnum = request.POST.get("contactnum")
            
            form = Customer( firstname=firstname, lastname = lastname, username =username,password = password, address = address, contactnum = contactnum)
            form.save()

            return redirect('my_customerRegistration_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')

class MyaddRoomView(View):
    def get(self, request):

        return render(request,'addRoom.html') 

    def post(self, request):
        form = RoomsForm(request.POST)

        if form.is_valid():
            roomtype = request.POST.get("roomtype")         
            timeslot = request.POST.get("timeslot")
            price = request.POST.get("price")
            
            form = Rooms( roomtype=roomtype, timeslot = timeslot, price =price)
            form.save()

            return redirect('my_adminDashboard_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')

class MyadminDashboardView(View):
    def get(self, request):
        rooms = Rooms.objects.all()
        context = {
            'rooms': rooms
        }

        return render(request,'adminDashboard.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                roomtype = request.POST.get("roomtype")
                timeslot = request.POST.get("timeslot")
                price = request.POST.get("price")
             
                
                update_room = Rooms.objects.filter(id = id).update(id = id, roomtype = roomtype, timeslot = timeslot, price = price)
                print(update_room)
                print('profile updated')
                return redirect('my_adminDashboard_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Rooms.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                #return HttpResponse ('post')
                return redirect('my_adminDashboard_view')

class MydashboardCustomerView(View):
    def get(self, request):
        customers = Customer.objects.all()
        context = {
            'customers': customers
        }

        return render(request,'dashboardCustomer.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                firstname = request.POST.get("firstname")
                lastname = request.POST.get("lastname")
                username = request.POST.get("username")
                password = request.POST.get("password")
                address = request.POST.get("address")
                contactnum = request.POST.get("contactnum")
             
                
                update_customer = Customer.objects.filter(id = id).update(id = id, firstname = firstname, lastname = lastname, username = username, password = password, address = address, contactnum = contactnum)
                print(update_customer)
                print('profile updated')
                return redirect('my_dashboardCustomer_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                customerdel = Customer.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                #return HttpResponse ('post')
                return redirect('my_dashboardCustomer_view')
            