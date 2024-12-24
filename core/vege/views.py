from django.shortcuts import render ,redirect

from .models import *

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')
        receipe_image =request.FILES.get('receipe_image')

        print(receipe_name)
        print(receipe_desc)
        print(receipe_image)
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_desc = receipe_desc,
            receipe_image = receipe_image)
        
        return redirect('/receipes/') 
    return render(request, 'receipes.html')