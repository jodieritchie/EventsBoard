from django import forms
from .models import Application, Job

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'short_description', 'long_description', 'job_post',  'company_address', 'company_size']
        # The other fields will be created automatically

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['notes']
        