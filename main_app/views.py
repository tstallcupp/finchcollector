from django.shortcuts import render

# Create your views here.

# Define home view
def home(request):
    return render(request, 'home.html')
