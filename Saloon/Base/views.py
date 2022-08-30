from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.
def make_feature_quote(quote):
    lines = []
    line = quote
    print(quote)
    line = list(line.split(' '))
    print(line)
    count = len(line)
    words = count//3
    cc = 0
    temp = ''
    for i in line:
        temp += i+' '
        cc += 1
        if cc >= words:
            lines.append(temp)
            cc = 0
            temp = ''
    if temp != '':
        lines[-1] += temp
        
    return lines

def home(request):
    featured = Featured.objects.get(is_active = True)
    quote_lines = make_feature_quote(featured.quote) 
    styles = list(Style.objects.all())
    if len(styles) > 3:
        styles = styles[0:3]
        
    #print(quote_lines)
    nav_class = {
        'home' : 'selected',
        'about' : '',
        'gallery' : '',
        'contact' : '',
    }
    context = {
        'featured' : featured,
        'quote_lines' : quote_lines,
        'styles' : styles,
        'nav_class' : nav_class
    }
    return render(request,'Base/index.html',context=context)

def about(request):
    nav_class = {
        'home' : '',
        'about' : 'selected',
        'gallery' : '',
        'contact' : '',
    }
    context = {
        'nav_class' : nav_class
    }
    return render(request,'Base/about.html',context)

def gallery(request):
    styles = Style.objects.all()

    nav_class = {
        'home' : '',
        'about' : '',
        'gallery' : 'selected',
        'contact' : '',
    }

    context = {
        'nav_class' : nav_class,
        'styles' : styles
    }
    return render(request , 'Base/gallery.html' , context= context)

def style(request , id):
    nav_class = {
        'home' : '',
        'about' : '',
        'gallery' : 'selected',
        'contact' : '',
    }
    style = Style.objects.get(id = id)

    context = {
        'nav_class' : nav_class,
        'style' : style
    }

    return render(request , 'Base/style.html',context)