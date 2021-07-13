from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models import Snack

admin.site.register(Snack)
