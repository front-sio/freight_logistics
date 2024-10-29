from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    CarouselItem, Service, About, Contact, TeamMember, Banner, 
    NewsletterSubscription, QuoteRequest
)
from .forms import QuoteRequestForm, NewsletterSubscriptionForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    carousel_items = CarouselItem.objects.filter(active=True)
    services = Service.objects.all()
    about = About.objects.first()
    contact = Contact.objects.first()
    team_members = TeamMember.objects.all()
    banner = Banner.objects.filter(page_name='home').first()

    if request.method == 'POST':
        newsletter_form = NewsletterSubscriptionForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, 'You have successfully subscribed to the newsletter!')
            return redirect('home')
        else:
            messages.error(request, 'Please provide a valid email address.')
    else:
        newsletter_form = NewsletterSubscriptionForm()

    context = {
        'carousel_items': carousel_items,
        'services': services,
        'about': about,
        'about_summary': about.get_summary() if about else '',
        'contact': contact,
        'team_members': team_members,
        'banner': banner,
        'newsletter_form': newsletter_form,
        'current_page': 'home',
    }
    return render(request, 'main/home.html', context)

def about_detail(request):
    about = get_object_or_404(About)
    banner = Banner.objects.filter(page_name='about_detail').first()
    context = {
        'about': about,
        'banner': banner,
        'current_page': 'about_detail',
    }
    return render(request, 'main/about_detail.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    banner = Banner.objects.filter(page_name='service_detail').first()
    context = {
        'service': service,
        'banner': banner,
        'current_page': 'service_detail',
    }
    return render(request, 'main/service_detail.html', context)

def services(request):
    banner = Banner.objects.filter(page_name='service').first()
    services = Service.objects.all()
    context = {
        'services': services,
        'banner': banner,
        'current_page': 'services',
    }
    return render(request, 'main/services.html', context)

def about(request):
    about = About.objects.first()
    banner = Banner.objects.filter(page_name='about').first()
    context = {
        'about': about,
        'banner': banner,
        'current_page': 'about',
    }
    return render(request, 'main/about.html', context)

def contact(request):
    contact = Contact.objects.first()
    banner = Banner.objects.filter(page_name='contact').first()
    
    if request.method == 'POST':
        quote_form = QuoteRequestForm(request.POST)
        if quote_form.is_valid():
            quote = quote_form.save()
            # Send email notification
            send_mail(
                'New Quote Request',
                f'Name: {quote.name}\nEmail: {quote.email}\nService: {quote.service}\nPhone: {quote.phone}\nMessage: {quote.message}',
                settings.EMAIL_HOST_USER,
                ['admin@sifongo.com'],  # Replace with your admin email
                fail_silently=False,
            )
            messages.success(request, 'Your quote request has been submitted successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        quote_form = QuoteRequestForm()

    context = {
        'contact': contact,
        'banner': banner,
        'quote_form': quote_form,
        'current_page': 'contact',
    }
    return render(request, 'main/contact.html', context)

# Additional Pages Views

def feature(request):
    banner = Banner.objects.filter(page_name='feature').first()
    context = {
        'banner': banner,
        'current_page': 'feature',
    }
    return render(request, 'main/feature.html', context)

def quote(request):
    # Assuming 'quote' is a separate page for requesting quotes
    if request.method == 'POST':
        quote_form = QuoteRequestForm(request.POST)
        if quote_form.is_valid():
            quote = quote_form.save()
            # Send email notification
            send_mail(
                'New Quote Request',
                f'Name: {quote.name}\nEmail: {quote.email}\nService: {quote.service}\nPhone: {quote.phone}\nMessage: {quote.message}',
                settings.EMAIL_HOST_USER,
                ['admin@sifongo.com'],  # Replace with your admin email
                fail_silently=False,
            )
            messages.success(request, 'Your quote request has been submitted successfully!')
            return redirect('quote')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        quote_form = QuoteRequestForm()

    context = {
        'quote_form': quote_form,
        'current_page': 'quote',
    }
    return render(request, 'main/quote.html', context)

def team(request):
    team_members = TeamMember.objects.all()
    banner = Banner.objects.filter(page_name='team').first()
    context = {
        'team_members': team_members,
        'banner': banner,
        'current_page': 'team',
    }
    return render(request, 'main/team.html', context)

def testimonial(request):
    testimonials = Testimonial.objects.all()  # Assuming you have a Testimonial model
    banner = Banner.objects.filter(page_name='testimonial').first()
    context = {
        'testimonials': testimonials,
        'banner': banner,
        'current_page': 'testimonial',
    }
    return render(request, 'main/testimonial.html', context)

def custom_404(request):
    return render(request, 'main/404.html', status=404)

# Admin Dashboard Views

@login_required
def admin_dashboard(request):
    # Replace the following with actual data retrieval
    context = {
        'total_users': 120,        # Example data
        'total_content': 45,       # Example data
        'total_reports': 10,       # Example data
        'current_page': 'admin_dashboard',
    }
    return render(request, 'admin/dashboard.html', context)

@login_required
def admin_users(request):
    users = User.objects.all()  # Assuming you have User model imported
    context = {
        'users': users,
        'current_page': 'admin_users',
    }
    return render(request, 'admin/users.html', context)

@login_required
def admin_content(request):
    services = Service.objects.all()
    context = {
        'services': services,
        'current_page': 'admin_content',
    }
    return render(request, 'admin/content.html', context)

@login_required
def admin_reports(request):
    reports = Report.objects.all()  # Assuming you have a Report model
    context = {
        'reports': reports,
        'current_page': 'admin_reports',
    }
    return render(request, 'admin/reports.html', context)

@login_required
def admin_settings(request):
    # Implement settings logic
    context = {
        'current_page': 'admin_settings',
    }
    return render(request, 'admin/settings.html', context)

@login_required
def admin_logout(request):
    logout(request)  # Make sure to import logout from django.contrib.auth
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')
