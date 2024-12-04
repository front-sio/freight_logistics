from django.http import HttpResponsePermanentRedirect

class RedirectToWWWMiddleware:
    """
    Middleware to redirect non-www requests (e.g., sifongo.co.tz) to www (e.g., www.sifongo.co.tz).
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        # Redirect only if the host is non-www
        if host == "sifongo.co.tz":
            return HttpResponsePermanentRedirect(f"https://www.sifongo.co.tz{request.get_full_path()}")
        return self.get_response(request)
