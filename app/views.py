from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os
from .models import *

# Create your views here.
def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def skills(req):
    return render(req,'skills.html')

def resume(req):
    file_path=os.path.join(
        settings.BASE_DIR,
        'app',
        'static',
        'resume',
        'govind_patel _resume.pdf'
    )
    return FileResponse(
        open(file_path, 'rb'),
        content_type='application/pdf'
    )
    
def contact(req):
    if req.method=="POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        subject=req.POST.get('subject')
        message=req.POST.get('message')
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return render(req,'contact.html',{'success':True})
    return render(req,'contact.html')   

def education(req):
    return render(req,'education.html')

def project(req):
    return render(req,'project.html')