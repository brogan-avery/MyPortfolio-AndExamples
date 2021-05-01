from django.contrib import admin

from .models import Element_levels
from .models import Temps
from .models import Scores
# Register your models here.

admin.site.register(Element_levels)
admin.site.register(Temps)
admin.site.register(Scores)