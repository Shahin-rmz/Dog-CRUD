from django.contrib import admin
from dogs.models import Dog
from dogs.models import Breed

# Register your models here.

admin.site.register(Dog)
admin.site.register(Breed)
