from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):

    SIZE_1_20 = 'size_1-20'
    SIZE_21_100 = 'size_21-100'
    SIZE_101_999 = 'size_101-999'
    SIZE_1000 = 'size_1000+'

    CHOICES_SIZE = (
        (SIZE_1_20, '1-20'),
        (SIZE_21_100, '21-100'),
        (SIZE_101_999, '101-999'),
        (SIZE_1000, '1000+'),
    )

    ACTIVE = 'active'
    CLOSED = 'closed'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (CLOSED, 'Closed'),
    )

    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField(blank=True, null=True) #Can be empty

    company_name = models.CharField(max_length=255)
    company_address=models.CharField(max_length=255, blank=True, null=True)
    company_zipcode=models.CharField(max_length=255, blank=True, null=True)
    company_place=models.CharField(max_length=255, blank=True, null=True)
    company_country=models.CharField(max_length=255, blank=True, null=True)
    company_size = models.CharField(max_length=20, choices=CHOICES_SIZE, default=SIZE_1_20)

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)
    
    # Create string representation of self to show title
    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)