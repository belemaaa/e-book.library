from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = "E-book Library System"
admin.site.site_title = "E-book Library System"

admin.site.register(models.Member)