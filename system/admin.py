from django.contrib import admin
from .models import Appointment, Department, Nurse, Status, User, Prescription

# Register your models here.

admin.site.register(Department)
admin.site.register(Nurse)
admin.site.register(Status)
admin.site.register(Prescription)



class AppointmentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'age', 'gender', 'phone', 'department', 'date', 'status', 'nurse')
    list_display_links=('name',)
admin.site.register(Appointment, AppointmentAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'first_name', 'last_name', 'email', 'speciality',)
    list_display_links=('username',)
admin.site.register(User, UserAdmin)