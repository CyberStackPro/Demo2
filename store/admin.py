from django.contrib import admin
from . import models
# from tags. import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(ordering='inventory', description='Inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


admin.site.register(models.Collection)

# admin.site.register(models.Product, ProductAdmin)

# admin.site.register(models.Customer)

admin.site.register(models.Cart)

admin.site.register(models.CartItem)

admin.site.register(models.Order)

admin.site.register(models.OrderItem)

admin.site.register(models.Address)

admin.site.register(models.Promotion)

# admin.site.register(models.Tag)

# admin.site.register(models.TaggedItem)
