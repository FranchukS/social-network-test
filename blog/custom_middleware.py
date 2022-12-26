import datetime

from django.contrib.auth.models import AnonymousUser


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        user = request.user
        if not user.is_anonymous:
            user.last_activity = datetime.datetime.now()
            user.save()

        return response
