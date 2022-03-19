from django.contrib import admin

from puestosdetrabajoapp.models import gerente, reponedor, cajero
# Register your models here.


admin.site.register(gerente)
admin.site.register(reponedor)
admin.site.register(cajero)