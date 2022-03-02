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

#class MyadminDashboardView(View):
#	def get(self, request):
#		return render(request,'adminDashboard.html', {})

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
                Fname = request.POST.get("Fname")
                Lname = request.POST.get("Lname")
                ContactNum = request.POST.get("ContactNum")
                Street = request.POST.get("Street")
                City_Municipality = request.POST.get("City_Municipality")
                Province = request.POST.get("Province")
                
                update_book = Customer.objects.filter(id = id).update(id = id, Fname = Fname, Lname = Lname, ContactNum = ContactNum, Street = Street, City_Municipality=City_Municipality,Province=Province)
                print(update_book)
                print('profile updated')
                return redirect('my_dashboard_customer_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Rooms.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                #return HttpResponse ('post')
                return redirect('my_adminDashboard_view')
            