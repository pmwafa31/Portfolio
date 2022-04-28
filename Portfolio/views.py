from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Portfolio.models import Project, Contact, ProjectDetail, ProjectImage
from django.template import loader
from django.core.mail import EmailMultiAlternatives
# Create your views here.


def index(request):
    projects = Project.objects.all
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Store contact information inside Contact model
        data = Contact()
        data.name = name
        data.email = email
        data.subject = subject
        data.message = message
        data.save()

        #Send message to email
        template = loader.get_template('contact_form.txt')
        context = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message,
        }
        message = template.render(context)
        email = EmailMultiAlternatives("Portfolio message", message, to=['wafajeril@gmail.com'])
        email.content_subtype = 'html'
        email.send()
        messages.success(request, 'Your message sent successfully.')
        return HttpResponseRedirect('/')

def project_details(request, project_id):
    project_detail = ProjectDetail.objects.get(project__id= project_id)
    project_image = ProjectImage.objects.filter(project__id = project_id)
    context = {
        'project_detail': project_detail,
        'project_images': project_image
    }
    return render(request, 'project_details.html', context)
