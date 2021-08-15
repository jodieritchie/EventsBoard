"""events_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

#Show this view when we go to the page
from apps.core.views import frontpage, signup, job_detail, add_job, apply_for_job, search, edit_job, landing_page

from apps.userprofile.views import dashboard, view_application, view_dashboard_job
from apps.core.api import api_search

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('frontpage/', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
    
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/application/<int:application_id>/', view_application, name='view_application'),
    path('dashboard/job/<int:job_id>/', view_dashboard_job, name='view_dashboard_job'),

    path('jobs/api/search/', api_search, name='api_search'),
    path('jobs/search/', search, name='search'),
    path('jobs/add/', add_job, name='add_job'),
    path('jobs/<int:job_id>/', job_detail, name='job_detail'),
    path('jobs/<int:job_id>/edit/', edit_job, name='edit_job'),
    path('jobs/<int:job_id>/apply_for_job/', apply_for_job, name='apply_for_job'),
]
