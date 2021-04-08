from django import forms
from .models import Appointment
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'



class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'speciality', 'password1', 'password2',)


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('name', 'age', 'gender', 'phone', 'email', 'department', 'date')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
                'type': 'number'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
            }),
            'email': forms.TextInput(attrs={
                'class': 'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
            }),
            'gender': forms.Select(attrs={
                'class': 'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
            }),
            'department': forms.Select(attrs={
                'class': 'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
            }),       
            'date': DateTimeInput(attrs={
                'class': 'w-full bg-white rounded border border-gray-300 focus:border-green-500 focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
            })
        }



class UpdateAppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('status', 'nurse')
        widgets = {
            'status': forms.Select(attrs={
                'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-green-500 focus:bg-transparent focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
            }),
            'nurse': forms.Select(attrs={
                'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-green-500 focus:bg-transparent focus:ring-2 focus:ring-green-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
            }),
           
        }


