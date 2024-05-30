from django.contrib import admin

# Import models to register admin
from .models import Finch, Feeding

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)
