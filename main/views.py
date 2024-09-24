from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CarouselItem, Service, About, Contact, TeamMember, Banner

def home(request):
    carousel_items = CarouselItem.objects.filter(active=True)
    services = Service.objects.all()
    about = About.objects.first()  # Fetch the first About object
    contact = Contact.objects.first()
    team_members = TeamMember.objects.all()
    banner = Banner.objects.filter(page_name='home').first()

    context = {
        'carousel_items': carousel_items,
        'services': services,
        'about': about,  # Pass the About object itself
        'about_summary': about.get_summary() if about else '',  # Summary of the About content
        'contact': contact,
        'team_members': team_members,
        'banner': banner,
    }
    return render(request, 'main/home.html', context)


def about_detail(request):
    about = get_object_or_404(About)
    banner = Banner.objects.filter(page_name='about_detail').first()
    return render(request, 'main/about_detail.html', {'about': about, 'banner': banner})

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    banner = Banner.objects.filter(page_name='service_detail').first()
    return render(request, 'main/service_detail.html', {'service': service, 'banner': banner})

def services(request):
    banner = Banner.objects.filter(page_name='service').first()
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services, 'banner': banner})

def about(request):
    about = About.objects.first()
    banner = Banner.objects.filter(page_name='about').first()
    return render(request, 'main/about.html', {'about': about, 'banner': banner})

def contact(request):
    contact = Contact.objects.first()
    banner = Banner.objects.filter(page_name='contact').first()
    return render(request, 'main/contact.html', {'contact': contact, 'banner': banner})







@login_required
def admin_dashboard(request):
    # Example data, replace with real queries
    context = {
        'total_users': 120,
        'total_content': 45,
        'total_reports': 10,
    }
    return render(request, 'admin/dashboard.html', context)

@login_required
def admin_users(request):
    # Code to manage users
    return render(request, 'admin/users.html')

@login_required
def admin_content(request):
    # Code to manage content
    return render(request, 'admin/content.html')

@login_required
def admin_reports(request):
    # Code to manage reports
    return render(request, 'admin/reports.html')

@login_required
def admin_settings(request):
    # Code to manage settings
    return render(request, 'admin/settings.html')

@login_required
def admin_logout(request):
    # Handle logout
    return render(request, 'admin/logout.html')

