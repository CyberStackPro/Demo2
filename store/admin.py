from django.contrib import admin
from . import models
from django.http.request import HttpRequest
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
# from tags. import models

# Register your models here.


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low'),
            ('>=10', 'OK')
        ]

    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        return queryset.filter(inventory__gte=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price',
                    'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    # prepopulated_fields = {'slug': ('title',)}
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update',
                   InventoryFilter]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory', description='Inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'email', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith',
                     'last_name__istartswith', 'email']

    @admin.display(description='Orders Count')
    def orders_count(self, customer):
        url = (reverse('admin:store_order_changelist')
               + '?' + urlencode({'customer__id': f'{customer.id}'}))
        return format_html('<a href="{}">{}</a>', url, customer.order_set.count())
        # Count the orders associated with this customer
        # return customer.order_set.count()


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']


# admin.site.register(models.Collection)

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (reverse('admin:store_product_changelist')
               + '?' + urlencode({'collection__id': f'{collection.id}'}))
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
        # return collection.products_count

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
