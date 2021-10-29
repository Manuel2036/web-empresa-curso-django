from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Ordem", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")



    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ['order','title'] 
 
    def __str__(self):
        return self.title 