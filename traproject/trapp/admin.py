from django.contrib import admin

# Register your models here.
from .models import Places
admin.site.register(Places)

from .models import Team
admin.site.register(Team)