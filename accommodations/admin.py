from django.contrib import admin
from .models import Category, Accommodation

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['name','slug','location','price','available','created','updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
