from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login , logout
from django.shortcuts import redirect
from .forms import FormLogin
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages
# from django.conf import settings
# from django.contrib.auth.decorators import login_required

# @login_required(login_url=settings.LOGIN_URL)
@requires_csrf_token
def login_view(request):
    form = FormLogin(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard/')
        else:
           
            messages.warning(request, "Username Atau Password Lu Salah")
            return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})

# @login_required(login_url=settings.LOGIN_URL)
def logoutview(request):
    logout(request)
    request.session.flush()
    return render(request, 'logout.html')
