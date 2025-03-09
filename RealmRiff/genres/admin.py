from django.contrib import admin
from . import models
# Register your models here.

class GenreFellowInline(admin.TabularInline):
    model = models.GenreFellow

admin.site.register(models.Genre)
