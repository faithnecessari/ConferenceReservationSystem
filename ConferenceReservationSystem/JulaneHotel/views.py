from django.shortcuts import render
from django.views.generic import View

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