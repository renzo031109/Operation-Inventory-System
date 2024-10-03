from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import logout

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
