from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-appointment/', views.CreateAppointmentView.as_view(), name='create-appointment'),
    path('appointments/', views.AppointMentList.as_view(), name='appointment-list'),
    path('appointments/<int:pk>', views.AppointmentUpdateView.as_view(), name='appointment-detail'),
    path('appointments/<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment-delete'),

    path('accounts/signup/', views.SignUpView.as_view(), name='account_signup'),

    # email
    path('appointments/<int:pk>/send/', views.SendEmailToPatientView.as_view(), name='send-email'),
]