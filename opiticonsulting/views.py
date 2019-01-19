from django.shortcuts import render 
from django.http import HttpResponseRedirect 

from .models import Demo, Service, Contact 
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request,'index.html') 

def service(request):
    serv = Service.objects.all()
    return render(request,'opiticonsulting/services.html', { 'serv':serv })

def demo(request):
    sols = Demo.objects.all()
    return render(request,'opiticonsulting/solutions.html', {'sols': sols }) 

def aboutUs(request):
    return render(request,'opiticonsulting/about-us.html',) 

def aboutFounder(request):
    return render(request,'opiticonsulting/aboutFounder.html',) 

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            cont = Contact(name=name,phone=phone,email=email,city=city,country=country,title=title,message=message)
            cont.save()
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    return render(request,'opiticonsulting/contact.html',{'form':form,})
