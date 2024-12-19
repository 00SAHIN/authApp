from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   
    peoples = [
        {'name': 'Sachin Sisodiya', 'age': 24},
        {'name': 'Robin', 'age': 26},
        {'name': 'Yash', 'age': 24},
        {'name': 'Rohini', 'age': 16},
    ]
    for people in peoples:
        if people['age']:
            print("Yes")
    text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem."""
    vegies=['potato', 'tomato',' onion',' cucumber', 'spinach', 'carrot']
    # Pass the text as part of the context dictionary
    return render(request, "home/index.html", context={'page':'Djnago2024tutorail','peoples': peoples, 'text': text, 'vegies': vegies})

def about(request):
    context={'page': 'About'}
    # Your view logic here
    return render(request , "home/about.html",context)

def contact(request):
    # Your view logic here
    context={'page': 'Contact'}
    return render(request , "home/contact.html",context)



def success_page(request):
    # Corrected the HTML and ensured it's well-formed
    return HttpResponse("<h1>This is a success page</h1>")
