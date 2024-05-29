from django.contrib import admin

# Import models to register admin
from .models import Finch

# Register your models here.
admin.site.register(Finch)
