from django.contrib import admin
from .models import WareHouse, Product

class WareHouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'qty', 'price']
    list_display_links = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'qty', 'mato', 'ip', 'tugma', 'zamok']
    list_display_links = ('id', 'name')

admin.site.register(Product, ProductAdmin)
admin.site.register(WareHouse, WareHouseAdmin)
