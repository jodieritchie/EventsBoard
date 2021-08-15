from django import forms
from .models import Application, Job

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'short_description', 'long_description', 'company_name', 'company_address', 'company_zipcode', 'company_place', 'company_country', 'company_size']
        # The other fields will be created automatically

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']
        