from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Project, Schedule
from django.contrib.auth.decorators import login_required


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


@login_required
def customer_dashboard(request):
    customer = request.user.customer
    projects = Project.objects.filter(customer=customer)
    schedules = Schedule.objects.filter(project__in=projects)
    context = {
        'customer': customer,
        'projects': projects,
        'schedules': schedules,
    }
    return render(request, 'projects/customer_dashboard.html', context)


def homepage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email (replace with your email settings)
            subject = f'New Contact Form Submission from {name}'
            message_body = f'Name: {name}\nEmail: {email}\n\n{message}'
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, ['gustavo.larcoj@gmail.com'])

            return redirect('homepage')  # Redirect after successful submission
    else:
        form = ContactForm()

    return render(request, 'projects/homepage.html', {'form': form})
