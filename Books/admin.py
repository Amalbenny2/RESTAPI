from django.contrib import admin
from Books import models

# Register your models here.
admin.site.register(models.Author),
admin.site.register(models.Book),