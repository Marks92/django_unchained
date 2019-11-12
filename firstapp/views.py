from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import People

def viewRegisterPage(request):
    template = "register.html"
    return render(request, template)


def addUser(request):

    if request.method['POST']:
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        age = request.POST.get('age')

        People.objects.create(first_name=firstName, last_name=lastName, age=age)
        return redirect('index')

    # Print the values
    return HttpResponse("firstname = %s, lastname = %s, age=%s" %(u.first_name, u.last_name, u.age))

def viewIndexPage(request):
    allPeople = People.objects.all()
    # send all people data to template
    context = {'people' : allPeople}
    template = "index.html"
    return render(request, template, context)
