from django import forms
from .models import *

class RoomsForm(forms.ModelForm):

    class Meta:
            model = Rooms
            fields= "__all__"


class CustomerForm(forms.ModelForm):

    class Meta:
            model = Customer
            fields= "__all__"