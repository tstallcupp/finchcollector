from django.shortcuts import render

finches = [
  {'name': 'Flick', 'species': 'zebra finch', 'description': 'energetic and lively', 'age': 1},
  {'name': 'Peep', 'species': 'society finch', 'description': 'sociable and friendly', 'age': 2},
  {'name': 'Tweet', 'species': 'gouldian finch', 'description': 'colorful and vibrant', 'age': 3},
  {'name': 'Chirp', 'species': 'star finch', 'description': 'calm and peaceful', 'age': 2},
  {'name': 'Flutter', 'species': 'spice finch', 'description': 'curious and playful', 'age': 1}
]

# Create your views here.

# Define home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })