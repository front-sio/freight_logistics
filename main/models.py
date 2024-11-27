from django.db import models

class CarouselItem(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='carousel/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

class About(models.Model):
    image = models.ImageField(upload_to='about/')
    content = models.TextField()

    def __str__(self):
        return "About Us"

    def get_summary(self, length=150):
        return self.content[:length] + '...' if len(self.content) > length else self.content

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_embed = models.TextField(help_text="Embed Google Maps iframe here.", null=True)

    def __str__(self):
        return "Contact Information"

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, null=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name

class Banner(models.Model):
    page_name = models.CharField(max_length=100, unique=True, null=True)
    title = models.CharField(max_length=255, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return f"Banner for {self.page_name}"

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email

class QuoteRequest(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    service = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20, null=True)
    message = models.TextField()
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote Request from {self.name} for {self.service}"



class AWB(models.Model):
    awb_number = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.awb_number

    def calculate_revenue(self):
        # Placeholder logic; replace with actual revenue calculation
        return sum(some_related_revenue.amount for some_related_revenue in self.revenues.all())

    def calculate_profit(self):
        revenue = self.calculate_revenue()
        total_cost = self.calculate_total_cost()
        return revenue - total_cost


class Cost(models.Model):
    awb = models.ForeignKey('AWB', on_delete=models.CASCADE, null=True, related_name='awbs')
    name = models.CharField(max_length=200, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)