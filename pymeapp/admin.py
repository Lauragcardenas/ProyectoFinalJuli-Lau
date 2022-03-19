from django.contrib import admin

from pymeapp.models import cliente, articulo, envio
# Register your models here.


admin.site.register(cliente)
admin.site.register(articulo)
admin.site.register(envio)