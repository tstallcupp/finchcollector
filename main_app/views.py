from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# finches = [
#   {'name': 'Flick', 'species': 'zebra finch', 'description': 'energetic and lively', 'age': 0},
#   {'name': 'Peep', 'species': 'society finch', 'description': 'sociable and friendly', 'age': 2},
#   {'name': 'Tweet', 'species': 'gouldian finch', 'description': 'colorful and vibrant', 'age': 3},
#   {'name': 'Chirp', 'species': 'star finch', 'description': 'calm and peaceful', 'age': 2},
#   {'name': 'Flutter', 'species': 'spice finch', 'description': 'curious and playful', 'age': 1}
# ]

# import finches from models instead
from .models import Finch

# Create your views here.

# Define home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })
    # return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch': finch })

# inherit from CreateView to create our own CBV used to create finches:
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'