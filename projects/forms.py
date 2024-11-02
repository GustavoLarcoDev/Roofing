from django import forms
from .models import Project, Customer, WorkTeam, Schedule


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
        fields = ['project', 'date', 'time', 'description']


class WorkTeamForm(forms.ModelForm):
    class Meta:
        model = WorkTeam
        fields = ['name', 'members']
