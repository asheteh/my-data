from django.contrib import admin
    
from .models import Orders

from .models import pma
admin.site.register(Orders)

admin.site.register(pma)
