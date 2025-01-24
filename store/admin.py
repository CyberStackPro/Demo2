from django.contrib import admin
from . import models
from django.http.request import HttpRequest
from django.db.models import Count
# from tags. import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price',
                    'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    # prepopulated_fields = {'slug': ('title',)}
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

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


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']


# admin.site.register(models.Collection)

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products_count

    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )

# admin.site.register(models.Product, ProductAdmin)

# admin.site.register(models.Customer)


admin.site.register(models.Cart)

admin.site.register(models.CartItem)

# admin.site.register(models.Order)

admin.site.register(models.OrderItem)

admin.site.register(models.Address)

admin.site.register(models.Promotion)

# admin.site.register(models.Tag)

# admin.site.register(models.TaggedItem)
