from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Project, Schedule, WorkTeam, Customer
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime


@user_passes_test(lambda u: u.is_superuser)
def admin_project_create(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        customer_id = request.POST.get('customer')
        status = request.POST.get('status')
        assigned_team_id = request.POST.get('assigned_team')

        customer = get_object_or_404(Customer, pk=customer_id)

        project = Project(
            address=address,
            customer=customer,
            status=status,
        )
        if assigned_team_id:
            assigned_team = get_object_or_404(WorkTeam, pk=assigned_team_id)
            project.assigned_team = assigned_team
        project.save()
        return redirect('admin_project_list')

    customers = Customer.objects.all()
    teams = WorkTeam.objects.all()
    context = {'customers': customers, 'teams': teams}
    return render(request, 'projects/admin_project_create.html', context)


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html',
                  {'projects': projects})


@login_required
def customer_dashboard(request):
    customer = request.user.customer
    projects = Project.objects.filter(customer=customer)
    schedules = Schedule.objects.filter(project__in=projects).order_by('date')
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
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL,
                      ['gustavo.larcoj@gmail.com'])

            return redirect('homepage')  # Redirect after successful submission
    else:
        form = ContactForm()

    return render(request, 'projects/homepage.html',
                  {'form': form, 'year': datetime.now().year})


def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {'project': project}
    return render(request, 'projects/project_detail.html', context)


@user_passes_test(lambda u: u.is_superuser)  # Only allow superusers
def admin_project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/admin_project_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_project_edit(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        # Get data from the form
        status = request.POST.get('status')
        assigned_team_id = request.POST.get('assigned_team')

        # Update the project
        project.status = status
        if assigned_team_id:
            assigned_team = get_object_or_404(WorkTeam, pk=assigned_team_id)
            project.assigned_team = assigned_team
        else:
            project.assigned_team = None
        project.save()
        return redirect('admin_project_list')  # Redirect after saving

    teams = WorkTeam.objects.all()
    context = {'project': project, 'teams': teams}
    return render(request, 'projects/admin_project_edit.html', context)
