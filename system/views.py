from django.shortcuts import render
from django.views import generic

from .forms import AppointmentForm, UpdateAppointmentForm
from django.shortcuts import reverse, redirect, get_object_or_404
from django.contrib import messages

from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Appointment
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from system.forms import CustomUserCreationForm
# Create your views here.
def home(request):
    return render(request, 'system/index.html')


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        messages.success(self.request, "Account Successfully Created")
        return reverse('account_login')


class CreateAppointmentView(generic.CreateView):
    form_class = AppointmentForm
    template_name = 'system/create_appointment.html'


    def get_success_url(self):
        messages.success(self.request, 'Appointment Successfully created. The Doctor will get back to you using your email address.')
        return reverse('home')


class AppointMentList(generic.ListView):
    template_name = 'system/appointment_list.html'
    context_object_name = 'appointments'


    def get_queryset(self):
        return Appointment.objects.filter(department=self.request.user.speciality).order_by('-created_at')


class AppointmentUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = UpdateAppointmentForm
    model = Appointment
    template_name = 'system/appointment_detail.html'

    def get_success_url(self):
        messages.success(self.request, 'Appointment status successfully updated')
        return reverse('appointment-list')



class AppointmentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Appointment

    def get_success_url(self):
        messages.success(self.request, 'Appointment successfully deleted!')
        return reverse('appointment-list')




class SendEmailToPatientView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        appointee = get_object_or_404(Appointment, pk=self.kwargs.get('pk'))
        context = {
            'person': appointee
        }
        return render(self.request, 'system/send_email.html', context)

    def post(self, *args, **kwargs):    
        subject = self.request.POST.get('subject')
        diagnosis = self.request.POST.get("diagnosis")
        prescription = self.request.POST.get('prescription')

        
        # get the person you are sending the message to
        appointee = get_object_or_404(Appointment, pk=self.kwargs.get('pk'))

        # render email to template
        msg_html = render_to_string('system/email.html', {
            'person': appointee,
            'diagnosis': diagnosis,
            'prescription': prescription
        })
        send_mail(
            subject=subject, 
            message='', 
            from_email=self.request.user.email, 
            recipient_list=[appointee.email],
            html_message=msg_html       
        )
        messages.success(self.request, 'You email has been sent')
        return redirect('appointment-list')

