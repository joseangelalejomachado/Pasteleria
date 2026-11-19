from django.db import models
from django.db import Q
# Create your models here.

class Pastel(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    #receta = models.OneToOneField("Receta", on_delete= models.CASCADE, related_name= "pasteles" , null=True, blank=True)

    class Meta:
        verbose_name = "Pastel"
        verbose_name_plural = "pasteles"
        constraints = [
            models.CheckConstraint(condition=models.Q(precio))
        ]
    def _str_(self):
            return f"{self.nombre} - {self.precio} - {self.descripcion}"
        



class Receta(models.Model):
    class Dificultad(models.TextChoices):
        FACIL = 'FAC', 'Fácil'
        MEDIO = 'MED', 'Medio'
        DIFICIL = 'DIF', 'Difícil'
        
    nombre = models.CharField(max_length=100)
    instrucciones = models.TextField()
    tiempo_realizacion = models.DurationField()
    dificultad = models.CharField(max_length=3, choices=Dificultad.choices, default=Dificultad.FACIL)
    receta_ingredientes = models.ManyToManyField('Ingrediente', through='RecetaIngrediente')
    pastel = models.OneToOneField(Pastel, on_delete=models.CASCADE, related_name="receta")
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
    
class RecetaIngrediente(models.Model):
    class Medida(models.TextChoices):
        LITROS = "L", "litros"
        GRAMOS = "G", "gramos"
    
    receta = models.ForeignKey('Receta', on_delete=models.CASCADE, related_name='ingredientes')
    ingrediente = models.ForeignKey('Ingrediente', on_delete=models.CASCADE, related_name='recetas')
    cantidad = models.IntegerField()
    medida = models.CharField(max_length=10, choices=Medida.choices, default=Medida.LITROS)
    
    class Meta:
        unique_together = ['receta', 'ingrediente']
        constraints = [
            
        ]
    def __str__(self) -> str:
        return f"{self.receta}, {self.ingrediente}, {self.cantidad}, {self.medida}"