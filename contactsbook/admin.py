from django.contrib import admin
from .models import Contacts

# registrar a(o) classe/model no admin.
admin.site.register(Contacts)