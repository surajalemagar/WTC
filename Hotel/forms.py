from django import forms
from .models import HotelInfo


class HotelForm(forms.ModelForm):

    class Meta():
        model = HotelInfo
        # fields = '__all__'
        fields=['Name','Address','phone_number','number_of_room']
