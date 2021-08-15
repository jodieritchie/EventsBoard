from .forms import AddJobForm, ApplicationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from apps.core.models import Job
from apps.userprofile.models import Userprofile
from django.contrib.auth.decorators import login_required

from .forms import AddJobForm, ApplicationForm

# Create your views here.

def search(request):
    return render(request, 'search.html')

def landing_page(request):
    return render(request, 'landing_page.html')

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'job_detail.html', {'job': job})

@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            return redirect('dashboard')
        
    else:
        # Else Return empty instance
        form = ApplicationForm()

    return render(request, 'apply_for_job.html', {'form': form, 'job': job})

@login_required    
def frontpage(request):
    jobs = Job.objects.filter(status=Job.ACTIVE).order_by('-created_at')
    return render(request, 'frontpage.html', {'jobs': jobs})

def signup(request):
    # Check if someone clicked the signup button
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')
            if account_type == 'employer':
                #Create user profile
                userprofile = Userprofile.objects.create(user=user, is_employer=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)
            return redirect('landing_page')
    else: 
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def add_job(request):
    # If it is submitted
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            # Create a new job in database
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            
            return redirect('dashboard')
    else: 
        form = AddJobForm()
        
    return render(request, 'add_job.html', {'form': form})


def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)
    # If it is submitted
    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)
        if form.is_valid():
            # Create a new job in database
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.save()
            
            return redirect('dashboard')
    else: 
        form = AddJobForm(instance=job)
        
    return render(request, 'edit_job.html', {'form': form, 'job': job})


