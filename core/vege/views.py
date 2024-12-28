from django.shortcuts import render, redirect
from django.contrib import messages  # Ensure this is imported
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Receipe

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')
        receipe_image = request.FILES.get('receipe_image')

        print(receipe_name)
        print(receipe_desc)
        print(receipe_image)
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_desc=receipe_desc,
            receipe_image=receipe_image)
        
        return redirect('/receipes/') 
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_desc = receipe_desc

        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect("/receipes/")
        
    context = {'receipes': queryset}
    return render(request, 'update_receipes.html', context)

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/') # Ensure messages framework is used correctly
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('/register/')
    return render(request, 'register.html')
