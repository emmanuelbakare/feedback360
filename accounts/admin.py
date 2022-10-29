from django.contrib import admin
from accounts.models import Person, Profile
# Register your models here.

admin.site.register(Profile)
admin.site.register(Person)
