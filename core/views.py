from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactCreationForm

# Create your views here.
def index(request):
    person = Contact.objects.all()
    context = {
        'person': person
    }
    return render(request, 'phonebook.html', context)

def create_contact(request):
    if request.method == 'POST':
        form = ContactCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ContactCreationForm()
        
    context = {
        'form': form
    }
    return render(request, 'contactForm.html', context)

def edit_contact(request, c_id):
    person =  get_object_or_404(Contact, pk=c_id)
    form = ContactCreationForm(request.POST, instance=person)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = ContactCreationForm(instance=person)
    context = {
        'form':form
    }
    return render(request, 'contactForm.html', context)

def read_contact(request, c_id):
    person = get_object_or_404(Contact, pk=c_id)
    return render(request, 'contact-detail.html', {'person': person})

def delete_contact(request, c_id):
    person = get_object_or_404(Contact, pk=c_id)
    person.delete()
    return redirect('home')
    
        