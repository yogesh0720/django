from django.contrib import admin

from .models import Question
admin.site.register(Question)

from .models import Choise
admin.site.register(Choise)

# Register your models here.
