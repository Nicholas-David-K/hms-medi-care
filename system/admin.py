from django.contrib import admin
from .models import Appointment, Department, Nurse, Status, User

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Department)
admin.site.register(Nurse)
admin.site.register(Status)




class UserAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email', 'speciality',)
    list_display_links=('first_name', 'email',)
admin.site.register(User, UserAdmin)