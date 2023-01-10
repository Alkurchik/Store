from django.contrib import admin

from products.models import ProductCategory, Product, Basket

# admin.site.register(Product)
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('name',)
    search_fields = ('name', 'description')
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0