from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Import finches from models instead
from .models import Finch, Twig
# Import the FeedingForm
from .forms import FeedingForm

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
    id_list = finch.twigs.all().values_list('id')
    twigs_finch_doesnt_have = Twig.objects.exclude(id__in=id_list)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'twigs': twigs_finch_doesnt_have })

# inherit from CreateView to create our own CBV used to create finches:
class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'species', 'description', 'age']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

# add this new function below finches_detail
def add_feeding(request, finch_id):
    # Create a ModelForm instance using the data that was submitted in the form 
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the cat_id assigned
        # We want a model instance, but can't save to db yet becasue we have not assigned the cat_id FK
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


class TwigList(ListView):
    model = Twig

class TwigDetail(DetailView):
    model = Twig

class TwigCreate(CreateView):
    model = Twig
    fields = '__all__'

def assoc_twig(request, finch_id, twig_id):
    Finch.objects.get(id=finch_id).twigs.add(twig_id)
    return redirect('detail', finch_id=finch_id)

