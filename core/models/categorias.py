from django.db import models

class Categorias(models.Model):
    categoria = models.CharField(max_length=100)


    def __str__(self):
        return f"({self.id}) {self.categoria} "