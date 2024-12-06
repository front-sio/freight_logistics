from django.http import HttpResponsePermanentRedirect

class EnforceWwwMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if not host.startswith('www.'):
            new_url = request.build_absolute_uri().replace(f'://{host}', f'://www.{host}')
            return HttpResponsePermanentRedirect(new_url)
        return self.get_response(request)
