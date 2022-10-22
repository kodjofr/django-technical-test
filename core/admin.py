from django.contrib import admin

# Register your models here.
from .models import Client, ComptesEspece, ImputationsEspeces

admin.site.register(Client)
admin.site.register(ComptesEspece)
admin.site.register(ImputationsEspeces)






