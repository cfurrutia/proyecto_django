from .models import Flan
from .forms import ContactFormModelForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def index(request):
    public_flans = Flan.objects.filter(is_private=False)
    context = {'public_flans': public_flans}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')
            else:
                messages.error(request)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)
    context = {'private_flans': private_flans}
    return render(request, 'welcome.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactFormModelForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')
