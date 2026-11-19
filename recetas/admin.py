from django.contrib import admin
from .models import Receta, Pastel, Ingrediente, RecetaIngrediente

# Register your models here.

admin.site.register(Receta)
admin.site.register(Pastel)
admin.site.register(Ingrediente)
admin.site.register(RecetaIngrediente)





