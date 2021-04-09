from django.contrib import admin
from .models import Car, Driven, Mod
# Register your models here.
admin.site.register(Car)
admin.site.register(Driven)
admin.site.register(Mod)