from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('user-login')


class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user

        # Redirect based on group
        if user.groups.filter(name='CLINIC').exists():
            return '/clinic/'  # URL for Clinic landing page
        elif user.groups.filter(name='OPERATION').exists():
            return '/'  # URL for Operation landing page
        else:
            return '/dashboard/'  # Default landing page if no groups matched







