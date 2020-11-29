from django.shortcuts import redirect, render


def register(request):
    if request.method == 'POST':
        # Register User
        return
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Register User
        return
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
