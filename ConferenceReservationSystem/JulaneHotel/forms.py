from django import forms
from .models import *

class RoomsForm(forms.ModelForm):

    class Meta:
            model = Rooms
            fields= "__all__"