from django import forms
from .models import Project, WorkTeam, Schedule
from django.contrib.auth.forms import UserCreationForm
from .models import Customer
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['address', 'customer', 'status', 'assigned_team']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['project', 'date', 'start_time', 'end_time']


class WorkTeamForm(forms.ModelForm):
    class Meta:
        model = WorkTeam
        fields = ['name']


class CustomerRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',
                  'email',
                  'first_name', 'last_name')  # Add any other fields you need

    def save(self, commit=True):
        user = super().save(commit=False)
        # Any additional logic for the User object (e.g., setting is_active)
        if commit:
            user.save()
            Customer.objects.create(user=user)  # Create the Customer object
        return user
