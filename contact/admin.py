from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id',
    # -id representa ordenar do jeito decrescente
    # list_filter = 'created_date'
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10  # o que é pra ser mostrado por página
    list_max_show_all = 200  # o máximo que é para ser mostrado
    list_editable = 'first_name', 'last_name',
    # editable e display links não podem ter os mesmos campos
    list_display_links = 'id', 'phone',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
