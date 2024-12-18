from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    peoples = [
        {'name': 'Sachin Sisodiya', 'age': 24},
        {'name': 'Robin', 'age': 26},
        {'name': 'Yash', 'age': 24},
        {'name': 'Rohini', 'age': 16},
    ]
    text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem."""
    
    # Pass the text as part of the context dictionary
    return render(request, "home/index.html", context={'peoples': peoples, 'text': text})

def success_page(request):
    # Corrected the HTML and ensured it's well-formed
    return HttpResponse("<h1>This is a success page</h1>")
