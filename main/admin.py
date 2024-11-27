from django.contrib import admin
from .models import (
    CarouselItem, Service, About, Contact, TeamMember, 
    Banner, NewsletterSubscription, QuoteRequest, AWB, Cost
)

@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    list_filter = ('active',)
    search_fields = ('title',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('content',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')
    search_fields = ('address', 'phone', 'email')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title')
    search_fields = ('page_name', 'title')

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at',)

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'phone', 'requested_at')
    search_fields = ('name', 'email', 'service', 'phone')
    readonly_fields = ('requested_at',)


@admin.register(AWB)
class AWBAdmin(admin.ModelAdmin):
    list_display = ['id', 'awb_number', 'created_at']
    search_fields = ['awb_number']


@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ['id', 'awb', 'name', 'amount']
    search_fields = ['name', 'awb__awb_number']
