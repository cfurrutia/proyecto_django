from django.shortcuts import render, redirect
from .models import ContactForm, Flan
from .forms import ContactFormModelForm


def index(request):
    public_flans = Flan.objects.filter(is_private=False)
    context = {'public_flans': public_flans}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', {})

def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'private_flans': private_flans})


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



