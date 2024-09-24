from django.db import models


# Carousel Model
class CarouselItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='carousel_images/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# Service Model
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/', blank=True)

    def __str__(self):
        return self.title

# About Model
class About(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True)

    def __str__(self):
        return "About Us Section"

    def get_summary(self):
        # Return a summary of the content (first 200 characters)
        return self.content[:200] + '...' if len(self.content) > 200 else self.content

# Contact Model
class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    image = models.ImageField(upload_to='contact_images/', blank=True)

    def __str__(self):
        return f"Contact - {self.email}"

# Team Member Model
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team_photos/')

    def __str__(self):
        return self.name



class Banner(models.Model):
    PAGE_CHOICES = [
        ('service_detail', 'Service Detail Page'),
        ('service', 'Service Page'),
        ('about', 'About Page'),
        ('about_detail', 'About Detail Page'),
    ]
    
    page_name = models.CharField(max_length=50, choices=PAGE_CHOICES, unique=True)
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_page_name_display()} Banner"
