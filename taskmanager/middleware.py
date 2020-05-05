"""Common middlewares."""

from django.conf import settings
from django.http import HttpResponseRedirect


class LoginRequiredMiddleware:
    """LoginRequiredMiddleware."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path.rstrip('/')
        if path != settings.LOGIN_URL and not request.user.is_authenticated:
            return HttpResponseRedirect(settings.LOGIN_URL)
        return self.get_response(request)
