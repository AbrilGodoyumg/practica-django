from django.db import models

# Create your models here.
class Tenis(models.Model):
    CHOICES=(                  #Variable, esto para convertir el CharField en un selector
        (24,"24"),
        (25,"25"),
        (26,"26"),
        (27,"27"),
    )
    talla=models.IntegerField(choices=CHOICES)
    nombre=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre}--{self.talla}--{self.precio}"