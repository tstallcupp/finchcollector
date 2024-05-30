from django.forms import ModelForm

# Import feeding from nextdoor
from .models import Feeding

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']