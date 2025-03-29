from django.contrib import admin

from main.models import Category, Order, Pet, Staff

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_editable = ('slug',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'category', 'breed', 'description', 'image')
    search_fields = ('name', 'age', 'category', 'breed', 'description', 'image')
    list_display_links = ('name', 'age', 'category', 'breed', 'description', 'image')
    ordering = ('category', 'name', )


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age', 'profession', 'image', 'description')
    search_fields = ('name', 'last_name','profession',)
    list_display_links = ('name', 'last_name', 'profession',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'animal', 'order_date')
    search_fields = ('name', 'phone')
    list_display_links = ('name', 'phone')
    