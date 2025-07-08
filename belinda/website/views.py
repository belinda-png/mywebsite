from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def home(request):

    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message_content = request.POST.get('message', '')
        
        if name and email and message_content:
            # Form data is valid
            try:
                # Configure this in your settings.py with your email credentials
                send_mail(
                    f'Portfolio Contact: Message from {name}',
                    f'Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}',
                    email,  # From email
                    [settings.DEFAULT_FROM_EMAIL],  # To email (your email)
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message! I will get back to you soon.')
            except Exception as e:
                # Handle email sending failure
                messages.error(request, 'There was a problem sending your message. Please try again later.')
                print(f"Email error: {e}")
        else:
            # Form data is invalid
            messages.error(request, 'Please fill out all fields correctly.')
            
    # For both GET requests and after processing POST
    context = {
        'page_title': 'Portfolio - Home',
    }
    return render(request, 'index.html', context)

def about(request):
   
    context = {
        'page_title': 'Portfolio - About Me',
    }
    return render(request, 'about.html', context)

def projects(request):
    """
    View for a separate projects page if you want to expand later
    """
    # You could fetch projects from a database here
    projects_list = [
        {
            'title': 'Portfolio Website',
            'description': 'A responsive portfolio website showcasing my projects and skills, built with Django, HTML, CSS, and JavaScript.',
            'github_url': 'https://github.com/yourusername/portfolio',
        },
        {
            'title': 'Task Manager App',
            'description': 'A single-page React app for managing daily tasks with a sleek user interface and localStorage data persistence.',
            'github_url': 'https://github.com/yourusername/task-manager',
        },
        {
            'title': 'Weather Dashboard',
            'description': 'A weather dashboard fetching real-time weather data from a public API, featuring search and geolocation.',
            'github_url': 'https://github.com/yourusername/weather-dashboard',
        },
    ]
    
    context = {
        'page_title': 'Portfolio - Projects',
        'projects': projects_list,
    }
    return render(request, 'projects.html', context)

def contact(request):
    """
    View for a separate contact page if you want to expand later
    """
    context = {
        'page_title': 'Portfolio - Contact',
    }
    return render(request, 'contact.html', context)