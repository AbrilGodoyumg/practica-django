from django.contrib import admin
from .models.prenda import Prenda
from .models.accesorios import Accesorio
from .models.tenis import Tenis

# Register your models here.
admin.site.register(Prenda) #Se registra la clase par que se pueda visualizar y realizar la migracion
admin.site.register(Accesorio)
admin.site.register(Tenis)