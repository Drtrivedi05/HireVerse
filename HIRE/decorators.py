# app_name/decorators.py
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def login_required_role(allowed_roles=None):
    """
    Ensures the user is logged in AND has one of the allowed roles.
    'allowed_roles' should be a list, e.g. ['admin', 'tnp'].
    """

    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            user_id = request.session.get('user_id')
            user_role = request.session.get('role')

            # ✅ Check login first
            if not user_id or not user_role:
                messages.error(request, "Please log in first.")
                return redirect('login')

            # ✅ Then check role
            if allowed_roles and user_role not in allowed_roles:
                messages.error(request, "You are not authorized to access this page.")
                return redirect('login')  # or redirect('index')

            # ✅ Allow access
            return view_func(request, *args, **kwargs)

        return _wrapped
    return decorator
