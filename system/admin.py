from django.contrib import admin
from .models import Doctor, Appointment, Department, Nurse, Status, User

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Department)
admin.site.register(Nurse)
admin.site.register(Status)
admin.site.register(User)