from django.contrib import admin
from todo.models import ToDo, Completion

# Register your models here.
admin.site.register(ToDo)
admin.site.register(Completion)
