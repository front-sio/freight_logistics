from django.contrib import admin
from .models import CarouselItem, Service, About, Contact, TeamMember, Banner

admin.site.register(CarouselItem)
admin.site.register(Service)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(TeamMember)



@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title')
    fields = ('page_name', 'image', 'title', 'description')

    def has_add_permission(self, request):
        # Limit the number of banners to one per page type
        if self.model.objects.count() >= len(self.model.PAGE_CHOICES):
            return False
        return super().has_add_permission(request)
