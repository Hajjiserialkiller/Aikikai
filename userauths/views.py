from django.shortcuts import redirect, render
from userauths.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from userauths.models import User
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created successfully!')
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return render(request, 'ecom/index.html')
    else:
        form = UserRegistrationForm()
        

    context = {
        'form': form,
    }
    return render(request, 'userauths/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in.')
        return redirect("ecom:index")
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in.')
                return redirect("ecom:index")
        except:
            messages.warning(request, f'User with {email} does not exist')


    return render(request, 'userauths/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect("ecom:index")