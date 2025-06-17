# middleware.py
# Django middleware that uses thread-local storage to keep track of the current user for the duration of a request.


import threading

_thread_locals = threading.local()

def get_current_user():
    return getattr(_thread_locals, 'user', None)

class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.user = request.user  # Store the current user
        response = self.get_response(request)
        return response
