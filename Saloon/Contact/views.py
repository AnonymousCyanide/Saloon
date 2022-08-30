from django.shortcuts import render , redirect
from .forms import ContactForm
# Create your views here.

def contact(request):
    nav_class = {
        'home' : '',
        'about' : '',
        'gallery' : '',
        'contact' : 'selected',
    }
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            print('Valid B')
            try :
                form.save()
                
                return redirect('contact_page')
            except :
                #messages.error(request, 'Invalid Credentials')
                return redirect('contact_page')
    
    context = {
        'nav_class' : nav_class,
        
    }
    return render(request , 'Contact/contact.html',context)