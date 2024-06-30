from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# id (primary key -- automático)

# Depois
# category (foreign key), show (boolean), picture (imagem)

# Depois
# owner (foreing key)
class Category(models.Model):
    class Meta:  # configuração de meta dados
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)  # para ser opcional
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)  # se vai mostrar
    # sua base de dados vai ter apenas o link apontando para o arquivo
    picture = models.ImageField(
        blank=True, upload_to='pictures/%Y/%m/')  # cria uma pasta picture
    # CASCADE é muito perigoso pois pode deletar todos
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )  # setados como nulo
    # da categoria família por exemplo
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
