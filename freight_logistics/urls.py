from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from ninja import NinjaAPI
from main.api import auth_router, protected_router

# Initialize Ninja API
ninja_api = NinjaAPI()


# Register Routers
ninja_api.add_router("/auth", auth_router)
ninja_api.add_router("/protected", protected_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cpanel/', include('sifongo.urls')),
    path('accounts/', include('accounts.urls')),
    path("api/", ninja_api.urls),    # Ninja API routes
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
