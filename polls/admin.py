from django.contrib import admin

# Register your models here.

# From Django
from django.contrib import admin

# My models
from polls.models import *

admin.site.register(Client)